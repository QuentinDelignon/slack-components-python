from typing import List , Union , Literal
from .commons import TextObject , ObjectWrapper

@ObjectWrapper
def Actions(elements: List, block_id: str = None):
    """A block that is used to hold interactive elements.

    Args:
        elements (List): An array of interactive element objects - buttons, select menus,
                         overflow menus, or date pickers. There is a maximum of 25 elements
                         in each action block.
        block_id (str, optional): A string acting as a unique identifier for a block. Defaults to None.
    """
    return {
            "type": "actions",
            "elements": elements,
            "block_id" : block_id
        }

@ObjectWrapper
def ContextBlock(elements: List, block_id: str = None):
    """Displays message context, which can include both images and text.

    Args:
        elements (List): An array of interactive element objects - buttons, select menus, 
                        overflow menus, or date pickers. There is a maximum of 25 elements
                        in each action block.
        block_id (str, optional): A string acting as a unique identifier for a block.
                                  Defaults to None.
    """
    return {
            "type": "context",
            "elements": elements,
            "block_id" :block_id
        }

@ObjectWrapper
def Divider(block_id: str = None):
    """A content divider, like an <hr>, to split up different blocks inside of a message.
    Args:
        block_id (str, optional): A string acting as a unique identifier for a block. Defaults to None.
    """
    return {
            "type": "divider",
            "block_id" : block_id
        }

@ObjectWrapper
def FileBlock(external_id: str, source: str = "remote", block_id: str = None):
    """Displays a remote file. You can't add this block to app surfaces directly, but it will show up when retrieving messages that contain remote files.

    Args:
        external_id (str): The external unique ID for this file.
        source (str, optional): At the moment, source will always be remote for a remote file.
        block_id (str, optional): A string acting as a unique identifier for a block. Defaults to None.
    """
    return {
            "type": "file",
            "external_id": external_id,
            "source": source,
            "block_id" : block_id
        }

@ObjectWrapper
def HeaderBlock(text : TextObject , block_id: str = None):
    """A header is a plain-text block that displays in a larger, bold font. Use it to delineate between different groups of content in your app's surfaces.  

    Args:
        text (TextObject) : text object to display
        block_id (str, optional): A string acting as a unique identifier for a block. Defaults to None.
    """
    return {
            "type": "header",
            "text" : text.dict(),
            "block_id" : block_id
        }

@ObjectWrapper
def ImageBlock(image_url : str , alt_text : str , title : TextObject = None , block_id : str = None):
    """A simple image block, designed to make those cat photos really pop.

    Args:
        image_url (str): The URL of the image to be displayed. Maximum length for this field is 3000 characters.
        alt_text (str): A plain-text summary of the image. This should not contain any markup. Maximum length for this field is 2000 characters.
        title (TextObject, optional): title for the image. Defaults to None.
        block_id (str, optional): A string acting as a unique identifier for a block. Defaults to None.
    """
    return {
        "type": "image",
        "image_url": image_url,
        "alt_text": alt_text,
        "block_id" : block_id,
        "title" : title
        }

@ObjectWrapper
def InputBlock(label : str , element : object , dispatch_action : bool = False , block_id : str = None , hint : TextObject = None , optional : bool = False):
    """A block that collects information from users - it can hold a plain-text input element, a checkbox element, a radio button element, a select menu element, a multi-select menu element, or a datepicker.

    Args:
        label (str): A label that appears above an input element in the form of a text object that must have type of plain_text. Maximum length for the text in this field is 2000 characters.
        element (object): A plain-text input element, a checkbox element, a radio button element, a select menu element, a multi-select menu element, or a datepicker.
        dispatch_action (bool, optional): A boolean that indicates whether or not the use of elements in this block should dispatch a block_actions payload. Defaults to false. Defaults to False.
        block_id (str, optional):A string acting as a unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. block_id should be unique for each message or view and each iteration of a message or view. If a message or view is updated, use a new block_id. Defaults to None.
        hint (TextObject, optional): An optional hint that appears below an input element in a lighter grey. It must be a text object with a type of plain_text. Maximum length for the text in this field is 2000 characters. Defaults to None.
        optional (bool, optional): A boolean that indicates whether the input element may be empty when a user submits the modal. Defaults to false. Defaults to False.
    """
    return {
        "type" : "input",
        "element": element,
        "label":label,
        "dispatch_action" : dispatch_action,
        "block_id" : block_id,
        "hint" : hint,
        "optional" : optional
    }

@ObjectWrapper
def SectionBlock(text : TextObject = None , block_id : str = None , fields : List[TextObject] = None, accessory : object = False ) :
    """A section is one of the most flexible blocks available - it can be used as a simple text block, in combination with text fields, 
    or side-by-side with any of the available block elements.

    Args:
        text (TextObject, optional): The text for the block, in the form of a text object. Minimum length for the text in this field is 1 and maximum length is 3000 characters. 
        This field is not required if a valid array of fields objects is provided instead. Defaults to None.
        block_id (str, optional): _description_. Defaults to None.
        fields (List[TextObject], optional): _description_. Defaults to None.
        accessory (object, optional): _description_. Defaults to False.
    """
    if text is None and fields is None:
        raise RuntimeError('Section Blocks needs a text object or a fields Object , got neither of these')
    return {
        "type" : "section",
        "text" : text,
        "block_id" : block_id,
        "fields" : fields,
        "accessory" : accessory
    }

@ObjectWrapper
def VideoBlock( title : TextObject , thumbnail_url : str ,  video_url : str ,
        alt_text : str , author_name : str = None , block_id : str = None ,
        description : TextObject = None , provider_icon_url : str = None , 
        provider_name : str = None ,  title_url : str = None ,
    ):
    """A video block is designed to embed videos in all app surfaces (e.g. link unfurls, messages, modals, App Home) — anywhere you can put blocks! 
    To use the video block within your app, you must have the links.embed:write scope.

    Args:
        title (str): Video title in plain text format. Must be less than 200 characters.
        thumbnail_url (str): The thumbnail image URL.
        video_url (str): The URL to be embedded. Must match any existing unfurl domains within the app and point to a HTTPS URL.
        alt_text (str): A tooltip for the video. Required for accessibility
        author_name (str, optional): Author name to be displayed. Must be less than 50 characters. Defaults to None.
        block_id (str, optional): A string acting as a unique identifier for a block. If not specified, one will be generated. 
            Maximum length for this field is 255 characters. block_id should be unique for each message and each iteration of a message. 
            If a message is updated, use a new block_id. Defaults to None.
        description (TextObject, optional): Description for video in plain text format. Defaults to None.
        provider_icon_url (str, optional): Icon for the video provider - ex. Youtube icon. Defaults to None.
        provider_name (str, optional): The originating application or domain of the video ex. Youtube. Defaults to None.
        title_url (str, optional): Video title in plain text format. Must be less than 200 characters. Defaults to None.
    """
    return {
        "type":"video",
        "title" : title.dict(),
        "thumbnail_url" : thumbnail_url,
        "video_url" : video_url,
        "alt_text" : alt_text,
        "author_name" : author_name,
        "block_id" : block_id,
        "description" : description,
        "provider_icon_url" : provider_icon_url,
        "provider_name" : provider_name,
        "title_url" : title_url
    }