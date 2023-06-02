from pydantic import BaseModel
from typing import Literal , Union , List
from functools import wraps


class TextObject(BaseModel):
    """An object containing some text, formatted either as plain_text or using mrkdwn, our proprietary 
    contribution to the much beloved Markdown standard."""

    type : Literal["plain_text","mrkdown"]
    """The formatting to use for this text object. Can be one of plain_textor mrkdwn."""

    text : str
    """The text for the block. This field accepts any of the standard text formatting markup when type is mrkdwn.
        The minimum length is 1 and maximum length is 3000 characters."""

    emoji : bool = False
    """Indicates whether emojis in a text field should be escaped into the colon emoji format. 
    This field is only usable when type is plain_text."""

class OptionObject(BaseModel):
    """An object that represents a single selectable item in a select menu, multi-select menu, checkbox group, radio button group, or overflow menu."""
    text : TextObject
    """A text object that defines the text shown in the option on the menu."""
    value : str
    """A unique string value that will be passed to your app when this option is chosen"""
    description : Union[TextObject,None]
    """A plain_text only text object that defines a line of descriptive text shown below the text field beside the radio button. """
    url : str
    """A URL to load in the user's browser when the option is clicked."""

class OptionGroupObject(BaseModel):
    """Provides a way to group options in a select menu or multi-select menu."""
    label : TextObject
    """A plain_text only text object that defines the label shown above this group of options."""
    options : List[OptionObject]
    """An array of option objects that belong to this specific group."""

class ConfirmDialogObject(BaseModel):
    """An object that defines a dialog that provides a confirmation step to any interactive element.
    This dialog will ask the user to confirm their action by offering a confirm and deny buttons."""
    title : TextObject
    """ plain_text-only text object that defines the dialog's title."""
    text : TextObject
    """A plain text-only text object that defines the explanatory text that appears in the confirm dialog."""
    confirm : TextObject
    """A plain_text-only text object to define the text of the button that confirms the action."""
    deny : TextObject
    """A plain_text-only text object to define the text of the button that cancels the action."""
    style : Literal['primary','danger']
    """Defines the color scheme applied to the confirm button."""

class DispatchActionObject(BaseModel):
    """Determines when a plain-text input element will return a block_actions interaction payload."""
    trigger_action_on : List[Literal['on_enter_pressed','on_character_entered']]
    """An array of interaction types that you would like to receive a block_actions payload for. Should be one or both of:

        on_enter_pressed — payload is dispatched when user presses the enter key while the input is in focus. 
        Hint text will appear underneath the input explaining to the user to press enter to submit.
        
        on_character_entered — payload is dispatched when a character is entered (or removed) in the input."""

class FilterObject(BaseModel):
    """Provides a way to filter the list of options in a conversations select menu or conversations multi-select menu."""
    include : List[Literal['im','mpim','private','public']]
    """Indicates which type of conversations should be included in the list. 
    When this field is provided, any conversations that do not match will be excluded"""

class InputParameterObject(BaseModel):
    """Contains information about an input parameter."""
    name : str
    """The name of the input parameter."""
    value : str
    """The value of the input parameter."""

class TriggerObject(BaseModel):
    """Contains information about a trigger."""
    url : str
    """A link trigger URL. Must be associated with a valid trigger."""
    customizable_input_parameters : List[InputParameterObject]
    """An array of input parameter objects. Each specified name must match an input parameter
    defined on the workflow of the provided trigger (url), and the input parameter mapping on 
    the trigger must be set as customizable: true. Each specified value must match the type defined
    by the workflow input parameter of the matching name."""

class WorkFlowObject(BaseModel):
    """Contains information about a workflow."""
    trigger : TriggerObject
    """A trigger object that contains information about a workflow's trigger."""

def ObjectWrapper(func):
    """Wrapper function to format data into a valid Slack API Object"""
    @wraps(func)
    def wrap(*args,**kwargs):
        res = func(*args,**kwargs)
        res = {k:v for k,v in res.items() if v is not None}
        for k ,v in res.items():
            try:
                res[k] = v.dict()
            except:
                pass
        return res
    return wrap