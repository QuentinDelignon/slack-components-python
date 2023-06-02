# Slack Components Python Library

This Library intends to help developpers working with Slack's API. With this you find evey [Blocks](https://api.slack.com/reference/block-kit/blocks) , [Elements](https://api.slack.com/reference/block-kit/block-elements) and [Composition Objects](https://api.slack.com/reference/block-kit/composition-objects) defined in slack's messaging API docs.  
**This Library avoids a bit of code redundency that one would encouter when working with json messages. It also provides inline documentation , type checking and default values to bootstrap your development with slack !**

## Installation
### Build the library as a wheel
```bash
python setup.py bdist_wheel
```
you will find the library as a wheel file in the ```./dist``` folder
### Install the library
```bash
pip install path/to/lib.whl
```
and you should be good to go !

## Quickstart
Lets use this lib in a slack bolt project ! If you need help setting this up , check out [Slack's Docs](https://slack.dev/bolt-python/tutorial/getting-started)

Let's create this message :
![image](/attachments/example_message.PNG)

```python
import slack_components as sc

test_message = sc.blocks.SectionBlock(
            text= sc.commons.TextObject(
                type="plain_text",
                text="This Component has been generated from the python Library !"
            ),
            accessory=sc.elements.Button(
                text= sc.commons.TextObject(
                    type="plain_text",
                    text="Cool !"
                ),
                action_id='button_click',
            )
        )
```
You will find a working example [here](/example.py)

# Documentation
The code is fully documented using docstring, you can generate a local web version using pdoc : 
```bash
pip install pdoc
pdoc slack_components
```
The output will give you a link with the whole documentation in a beautiful and interactive website.