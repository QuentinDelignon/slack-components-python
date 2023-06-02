from typing import Literal , List
from .commons import TextObject , ObjectWrapper , OptionObject , ConfirmDialogObject , DispatchActionObject , OptionGroupObject , WorkFlowObject

@ObjectWrapper
def Button(
    text : TextObject, 
    action_id : str ,
    url : str = None , 
    value : str = None , 
    style : Literal['primary','danger'] = None,
    confirm : object = None , 
    acessibility_label : TextObject = None
) :
    """An interactive component that inserts a button. The button can be a trigger for anything from opening a simple link to starting a complex workflow.

    Args:
        text (TextObject): A text object that defines the button's text. Can only be of type: plain_text.
            text may truncate with ~30 characters. Maximum length for the text in this field is 75 characters.
        action_id (str): An identifier for this action. You can use this when you receive an interaction payload to identify the source of the action.
            Should be unique among all other action_ids in the containing block. Maximum length for this field is 255 characters.
        url (str, optional): A URL to load in the user's browser when the button is clicked. Maximum length for this field is 3000 characters. 
            If you're using url, you'll still receive an interaction payload and will need to send an acknowledgement response. Defaults to None.
        value (str, optional): The value to send along with the interaction payload. Maximum length for this field is 2000 characters. Defaults to None.
        style (Literal[&#39;primary&#39;,&#39;danger&#39;], optional): Decorates buttons with alternative visual color schemes.
            Use this option with restraint. Defaults to 'default'.
        confirm (object, optional): A confirm object that defines an optional confirmation dialog after the button is clicked. Defaults to None.
        acessibility_label (TextObject, optional): A label for longer descriptive text about a button element. 
            This label will be read out by screen readers instead of the button text object. Maximum length for this field is 75 characters. Defaults to None.
    """
    return {
        "type" : "button",
        "text": text,
        "action_id" : action_id,
        "url" : url,
        "value" : value,
        "style" : style,
        "confirm" : confirm,
        "acessibility_label" : acessibility_label
    }

@ObjectWrapper
def CheckBoxGroup(
    action_id : str , 
    options : OptionObject , 
    initial_options : List[OptionObject] = None,
    confirm : ConfirmDialogObject = None, 
    focus_on_load : bool = False
):
    """A checkbox group that allows a user to choose multiple items from a list of possible options.

    Args:
        action_id (str): An identifier for the action triggered when the checkbox group is changed.
        options (OptionObject): An array of option objects. A maximum of 10 options are allowed.
        initial_options (List[OptionObject], optional): An array of option objects that exactly matches one or more of
            the options within options. These options will be selected when the checkbox group initially loads.. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears after 
            clicking one of the checkboxes in this element. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. 
            Only one element can be set to true. Defaults to False.
    """
    return {
        "type":"checkboxes",
        "action_id" : action_id,
        "options" : options,
        "initial_options" : initial_options,
        "confirm" : confirm,
        "focus_on_load" : focus_on_load
    }

@ObjectWrapper
def DatePicker(
    action_id : str , 
    initial_date : str = None ,
    confirm : ConfirmDialogObject = None , 
    focus_on_load : bool = False ,
    placeholder : TextObject = None
):
    """An element which lets users easily select a date from a calendar style UI.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected.
        initial_date (str, optional): The initial date that is selected when the element is loaded. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears after a date is selected. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown on the datepicker. Defaults to None.
    """
    return {
        "type" : "datepicker",
        "action_id" : action_id,
        "initial_date" : initial_date,
        "confirm" : confirm,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def DateTimePicker(
    action_id : str , 
    initial_date_time : str = None ,
    confirm : ConfirmDialogObject = None , 
    focus_on_load : bool = False 
):
    """An element that allows the selection of both a date and a time of day formatted as a Unix timestamp.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected.
        initial_date_time (str, optional): The initial date and time that is selected when the element is loaded, represented as a UNUIX timestamp in seconds.
            This should be in the format of 10 digits, for example 1628633820 represents the date and time August 10th, 2021 at 03:17pm PST. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears after a date is selected. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to False.
    """
    return {
        "action_id" : action_id,
        "initial_date_time" : initial_date_time,
        "confirm" : confirm,
        "focus_on_load" : focus_on_load
    }

@ObjectWrapper
def EmailInput(
    action_id :  str ,
    initial_value : str  = None , 
    dispatch_action_config : DispatchActionObject = None , 
    focus_on_load : bool = False , 
    placeholder : TextObject = None
):
    """Text input dedicated to email

    Args:
        action_id (str): An identifier for the input value when the parent modal is submitted.
        initial_value (str, optional): The initial value in the email input when it is loaded. Defaults to None.
        dispatch_action_config (DispatchActionObject, optional): A dispatch configuration object that determines when during text input
            the element returns a block_actions payload. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Only one element
            can be set to true. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown in the email input. Defaults to None.
    """
    return {
        "type" : "email_text_input",
        "action_id" : action_id,
        "initial_value" : initial_value,
        "dispatch_action_config" : dispatch_action_config,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def Image(image_url : str , alt_text : str):
    """An element to insert an image as part of a larger block of content. 
    If you want a block with only an image in it, you're looking for the image block.

    Args:
        image_url (str): The URL of the image to be displayed.
        alt_text (str): A plain-text summary of the image. This should not contain any markup.
    """
    return {
        "type" : "image",
        "image_url" : image_url,
        "alt_text" : alt_text
    }

@ObjectWrapper
def MultiSelectStatic(
    action_id : str,
    options : List[OptionObject],
    option_groups : List[OptionGroupObject] = None,
    initial_options : List[OptionObject] = None,
    confirm : ConfirmDialogObject = None,
    max_selected_items : int = None,
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """This is the simplest form of select menu, with a static list of options passed in when defining the element.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. 
        options (List[OptionObject]): An array of option objects. 
        option_groups (List[OptionGroupObject], optional): An array of option group objects. Defaults to None.
        initial_options (List[OptionObject], optional): An array of option objects that exactly match one or more of 
            the options within options or option_groups. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted. Defaults to None.
        max_selected_items (int, optional): Specifies the maximum number of items that can be selected in the menu. Minimum number is 1. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown on the menu. Defaults to None.
    """
    return {
        "type": "multi_static_select",
        "action_id" : action_id,
        "options" : options , 
        "option_groups" : option_groups , 
        "initial_options" : initial_options,
        "confirm" : confirm,
        "max_selected_items" : max_selected_items,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def MultiSelectExternal(
    action_id : str,
    min_query_length :int,
    initial_options : List[OptionObject] = None,
    confirm : ConfirmDialogObject = None,
    max_selected_items : int = None,
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """This menu will load its options from an external data source, allowing for a dynamic list of options.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. 
        min_query_length (int): When the typeahead field is used, a request will be sent on every character change.
            If you prefer fewer requests or more fully ideated queries, use the min_query_length attribute to tell Slack
            the fewest number of typed characters required before dispatch. The default value is 3.
        initial_options (List[OptionObject], optional): An array of option objects that exactly match one or more of 
            the options within options or option_groups. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears before the 
            multi-select choices are submitted. Defaults to None.
        max_selected_items (int, optional): Specifies the maximum number of items that can be selected in the menu. 
            Minimum number is 1. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. 
            Only one element can be set to true. Defaults to false. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown on the menu. Defaults to None.
    """
    return {
        "type": "multi_external_select",
        "action_id" : action_id,
        "min_query_length" : min_query_length ,
        "initial_options" : initial_options,
        "confirm" : confirm,
        "max_selected_items" : max_selected_items,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def MultiSelectUsers(
    action_id : str,
    initial_users : List[str] = None,
    confirm : ConfirmDialogObject = None,
    max_selected_items : int = None,
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """This multi-select menu will populate its options with a list of Slack users visible to the current user in the active workspace.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. 
        initial_users (List[str], optional): An array of user IDs of any valid users to be pre-selected when the menu loads. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted. Defaults to None.
        max_selected_items (int, optional): Specifies the maximum number of items that can be selected in the menu. Minimum number is 1. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown on the menu. Defaults to None.
    """
    return {
        "type": "multi_users_select",
        "action_id" : action_id,
        "initial_users" : initial_users,
        "confirm" : confirm,
        "max_selected_items" : max_selected_items,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def MultiSelectConversations(
    action_id : str,
    initial_conversations : List[str] = None,
    default_to_current_conversation : bool = False,
    confirm : ConfirmDialogObject = None,
    max_selected_items : int = None,
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """This multi-select menu will populate its options with a list of public and private channels, DMs, and MPIMs visible to the current user in the active workspace.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. 
        initial_conversations (List[str]): An array of one or more IDs of any valid conversations to be pre-selected when the menu loads. 
            If default_to_current_conversation is also supplied, initial_conversations will be ignored. 
        default_to_current_conversation (bool, optional): Pre-populates the select menu with the conversation that the user was viewing when they opened the modal, 
            if available. Defaults to False.
        initial_options (List[OptionObject], optional): An array of option objects that exactly match one or more of 
            the options within options or option_groups. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted. Defaults to None.
        max_selected_items (int, optional): Specifies the maximum number of items that can be selected in the menu. Minimum number is 1. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown on the menu. Defaults to None.
    """
    return {
        "type": "multi_conversations_select",
        "action_id" : action_id,
        "initial_conversations" : initial_conversations,
        "default_to_current_conversation" : default_to_current_conversation,
        "confirm" : confirm,
        "max_selected_items" : max_selected_items,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def MultiSelectChannels(
    action_id : str,
    initial_channels : List[str] = None,
    confirm : ConfirmDialogObject = None,
    max_selected_items : int = None,
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """This multi-select menu will populate its options with a list of public channels visible to the current user in the active workspace.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. 
        initial_channels (List[str], optional): An array of one or more IDs of any valid public channel to be pre-selected when the menu loads. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted. Defaults to None.
        max_selected_items (int, optional): Specifies the maximum number of items that can be selected in the menu. Minimum number is 1. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown on the menu. Defaults to None.
    """
    return {
        "type": "multi_static_select",
        "action_id" : action_id,
        "initial_channels" : initial_channels,
        "confirm" : confirm,
        "max_selected_items" : max_selected_items,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def NumberInput(
    action_id : str ,
    is_decimal_allowed : bool = True,
    initial_value : str = None,
    min_value : str = None,
    max_value : str = None,
    dispatch_action_config : DispatchActionObject = None, 
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """This input elements accepts both whole and decimal numbers.

    Args:
        action_id (str): An identifier for the input value when the parent modal is submitted.
        is_decimal_allowed (bool, optional): Whether floats are accepted. Defaults to True.
        initial_value (str, optional): The initial value in the plain-text input when it is loaded. Defaults to None.
        min_value (str, optional): minimum value. Defaults to None.
        max_value (str, optional): maximum value. Defaults to None.
        dispatch_action_config (DispatchActionObject, optional): A dispatch configuration object that determines when during 
            text input the element returns a block_actions payload. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Defaults to False.
        placeholder (TextObject, optional):A plain_text only text object that defines the placeholder text shown in the number input. Defaults to None.
    """
    return {
        "type" : "number_input",
        "action_id" : action_id,
        "is_decimal_allowed" : is_decimal_allowed,
        "initial_value" : initial_value,
        "min_value" : min_value,
        "max_value" :max_value,
        "dispatch_action_config" : dispatch_action_config,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def OverflowMenu(
    action_id : str, 
    options : List[OptionObject],
    confirm : ConfirmDialogObject = None
):
    """when a user clicks on this overflow button, they will be presented with a list of options to choose from

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected
        options (List[OptionObject]): An array of up to five option objects to display in the menu.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that 
            appears after a menu item is selected. Defaults to None.
    """
    return {
        "type" : "overflow",
        "action_id" : action_id,
        "options" : options,
        "confirm" : confirm
    }

@ObjectWrapper
def PlainTextInput(
    action_id : str ,
    initial_value : str = None,
    multiline : bool = False,
    min_length : int = None,
    max_length : int = None ,
    dispatch_action_config : DispatchActionObject = None,
    focus_on_load : bool = False, 
    placeholder : TextObject = None
):
    """A plain-text input, similar to the HTML input tag, creates a field where a user can enter freeform data.

    Args:
        action_id (str): action's id
        initial_value (str, optional): initial value of the input. Defaults to None.
        multiline (bool, optional): whether user can write multiple lines. Defaults to False.
        min_length (int, optional): minimum length for valid text. Defaults to None.
        max_length (int, optional): maximum length for valid text. Defaults to None.
        dispatch_action_config (DispatchActionObject, optional): A dispatch configuration object that determines 
            when during text input the element returns a block_actions payload.. Defaults to None.
        focus_on_load (bool, optional): whether input should be focused on entering. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder 
            text shown in the plain-text input. Defaults to None.
    """
    return {
        "type":"plain_text_input",
        "action_id" : action_id,
        "initial_value" :initial_value,
        "multiline" : multiline,
        "min_length" : min_length,
        "max_length" : max_length,
        "dispatch_action_config" : dispatch_action_config,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def RadioButtonGroup(
    action_id : str ,
    options : List[OptionObject],
    initial_options : OptionObject,
    confirm : ConfirmDialogObject,
    focus_on_load : bool
):
    """ Visit https://api.slack.com/reference/block-kit/block-elements#radio for more details"""
    return {
        "type":"radio_buttons",
        "action_id" : action_id,
        "options" : options,
        "initial_options" : initial_options,
        "confirm" : confirm,
        "focus_on_load" : focus_on_load
    }

@ObjectWrapper
def SelectStatic(
    action_id : str,
    options : List[OptionObject],
    option_groups : List[OptionGroupObject] = None,
    initial_option : OptionObject = None,
    confirm : ConfirmDialogObject = None,
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """This is the simplest form of select menu, with a static list of options passed in when defining the element.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. 
        options (List[OptionObject]): An array of option objects. 
        option_groups (List[OptionGroupObject], optional): An array of option group objects. Defaults to None.
        initial_option (OptionObject, optional): option object that exactly match one or more of 
            the options within options or option_groups. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown on the menu. Defaults to None.
    """
    return {
        "type": "multi_static_select",
        "action_id" : action_id,
        "options" : options , 
        "option_groups" : option_groups , 
        "initial_option" : initial_option,
        "confirm" : confirm,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def SelectExternal(
    action_id : str,
    min_query_length :int,
    initial_option : OptionObject = None,
    confirm : ConfirmDialogObject = None,
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """This menu will load its options from an external data source, allowing for a dynamic list of options.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. 
        min_query_length (int): When the typeahead field is used, a request will be sent on every character change.
            If you prefer fewer requests or more fully ideated queries, use the min_query_length attribute to tell Slack
            the fewest number of typed characters required before dispatch. The default value is 3.
        initial_option (OptionObject, optional): option object that exactly match one or more of 
            the options within options or option_groups. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears before the 
            multi-select choices are submitted. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. 
            Only one element can be set to true. Defaults to false. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown on the menu. Defaults to None.
    """
    return {
        "type": "multi_external_select",
        "action_id" : action_id,
        "min_query_length" : min_query_length ,
        "initial_option" : initial_option,
        "confirm" : confirm,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def SelectUsers(
    action_id : str,
    initial_user : str = None,
    confirm : ConfirmDialogObject = None,
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """This multi-select menu will populate its options with a list of Slack users visible to the current user in the active workspace.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. 
        initial_user (str, optional): user ID of any valid users to be pre-selected when the menu loads. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted. Defaults to None.
        max_selected_items (int, optional): Specifies the maximum number of items that can be selected in the menu. Minimum number is 1. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown on the menu. Defaults to None.
    """
    return {
        "type": "multi_users_select",
        "action_id" : action_id,
        "initial_users" : initial_user,
        "confirm" : confirm,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def SelectConversations(
    action_id : str,
    initial_conversation : str = None,
    default_to_current_conversation : bool = False,
    confirm : ConfirmDialogObject = None,
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """This multi-select menu will populate its options with a list of public and private channels, DMs, and MPIMs visible to the current user in the active workspace.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. 
        initial_conversation (List[str]): ID of any valid conversations to be pre-selected when the menu loads. 
            If default_to_current_conversation is also supplied, initial_conversations will be ignored. 
        default_to_current_conversation (bool, optional): Pre-populates the select menu with the conversation that the user was viewing when they opened the modal, 
            if available. Defaults to False.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown on the menu. Defaults to None.
    """
    return {
        "type": "multi_conversations_select",
        "action_id" : action_id,
        "initial_conversation" : initial_conversation,
        "default_to_current_conversation" : default_to_current_conversation,
        "confirm" : confirm,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def SelectChannels(
    action_id : str,
    initial_channel : str = None,
    confirm : ConfirmDialogObject = None,
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """This multi-select menu will populate its options with a list of public channels visible to the current user in the active workspace.

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. 
        initial_channel (str, optional): An array of one or more IDs of any valid public channel to be pre-selected when the menu loads. Defaults to None.
        confirm (ConfirmDialogObject, optional): A confirm object that defines an optional confirmation dialog that appears before the multi-select choices are submitted. Defaults to None.
        focus_on_load (bool, optional): Indicates whether the element will be set to auto focus within the view object. Only one element can be set to true. Defaults to false. Defaults to False.
        placeholder (TextObject, optional): A plain_text only text object that defines the placeholder text shown on the menu. Defaults to None.
    """
    return {
        "type": "multi_static_select",
        "action_id" : action_id,
        "initial_channel" : initial_channel,
        "confirm" : confirm,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def TimePicker(
    action_id : str,
    initial_time : str = None,
    confirm : ConfirmDialogObject = None,
    focus_on_load : bool = False , 
    placeholder : TextObject = None,
    timezone : str = None
):
    """Visit https://api.slack.com/reference/block-kit/block-elements#timepicker for more informations"""
    return {
        "type" : "timepicker",
        "action_id" : action_id,
        "initial_time" : initial_time,
        "confirm" : confirm,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder ,
        "timezone" : timezone
    }

@ObjectWrapper
def URLInput(
    action_id : str ,
    initial_value : str = None,
    dispatch_action_config : DispatchActionObject = None,
    focus_on_load : bool = False,
    placeholder : TextObject = None
):
    """Visit https://api.slack.com/reference/block-kit/block-elements#url for more informations"""
    return {
        "type": "url_text_input",
        "action_id" : action_id,
        "initial_value" : initial_value ,
        "dispatch_action_config" : dispatch_action_config,
        "focus_on_load" : focus_on_load,
        "placeholder" : placeholder
    }

@ObjectWrapper
def WorkflowButton(
    text: TextObject,
    workflow : WorkFlowObject,
    accessibility_label : str,
    style : Literal["primary","danger"] = None
):
    """Visit https://api.slack.com/reference/block-kit/block-elements#workflow_button for more informations"""
    return {
        "type" : "workflow_button",
        "text" : text,
        "workflow" : workflow,
        "style" : style,
        "accessibility_label" :accessibility_label
    }