#   Copyright (c) 2006-2007 Open Source Applications Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from windmill.dep import json
from windmill.dep import functest
from datetime import datetime
from windmill.authoring import WindmillTestClient

def test_wmunti1():
    client = WindmillTestClient(__name__, assertions=False)
    
    assert client.open(url=u'http://tutorial.getwindmill.com/windmill-unittests/unit_tester.html')['result']
    assert client.click(id=u'subBtn')['result']
    
    # Tests that sleeps actually wait for long enough
    start = datetime.now()
    assert client.waits.sleep(milliseconds=u'3000')['result']
    end = datetime.now()
    print (end - start)
    assert ( end - start ).seconds >= 3
    assert client.asserts.assertText(validator=u'', id=u'sleeper')['result']
        
    # Tests that an 8 second sleep actually waits long enough
    start = datetime.now()
    assert client.waits.sleep(milliseconds=u'8000')['result']
    end = datetime.now()
    print (end - start)
    assert ( end - start ).seconds >= 8
    
    #execIDEJS and storeURL test
    assert client.storeURL(link='AwesomeLink')
    assert client.execIDEJS(js='windmill.varRegistry.items["{$AwesomeLink}"] = windmill.varRegistry.items["{$AwesomeLink}"].replace(\'http\', \'abcd\');')
    assert client.asserts.assertJS(js="'{$AwesomeLink}' == 'abcd://www.awesome.com/';")
    #unit tests for select by value
    assert client.select(val='d', id='flavor')['result']
    assert client.asserts.assertSelected(validator='d', id='flavor')['result']
    
    assert client.asserts.assertText(validator=u'Slept', id=u'sleeper')['result']
    assert client.type(text=u'my test text', id=u'junkfield')['result']
    assert client.asserts.assertValue(validator=u'my test text', id=u'junkfield')['result']
    assert client.radio(id=u'cougar')['result']
    assert client.asserts.assertChecked(id=u'cougar')['result']
    assert client.radio(id=u'duck')['result']
    assert client.asserts.assertChecked(id=u'duck')['result']
    assert client.check(id=u'Smallpox')['result']
    assert client.asserts.assertChecked(id=u'Smallpox')['result']
    assert not client.asserts.assertChecked(id=u'Mumps')['result']
    assert not client.asserts.assertChecked(id=u'Dizziness')['result']
    assert client.check(id=u'Mumps')['result']
    assert client.asserts.assertChecked(id=u'Mumps')['result']
    assert not client.asserts.assertChecked(id=u'Dizziness')['result']
    assert client.check(id=u'Dizziness')['result']
    assert client.asserts.assertChecked(id=u'Dizziness')['result']
    assert client.type(text=u'The text area tester', name=u'story')['result']
    assert client.asserts.assertValue(validator=u'The text area tester', id=u'story')['result']
    assert client.select(option=u'Strawberry', id=u'flavor')['result']
    assert client.asserts.assertSelected(validator=u'b', id=u'flavor')['result']
    assert client.select(option=u'Rum and Raisin', id=u'flavor')['result']
    assert client.asserts.assertSelected(validator=u'c', id=u'flavor')['result']
    assert not client.asserts.assertSelected(validator=u'd', id=u'flavor')['result']
    assert client.select(option=u'Peach and Orange', id=u'flavor')['result']
    assert client.asserts.assertSelected(validator=u'd', id=u'flavor')['result']
    assert client.click(id=u'clickme')['result']
    assert client.asserts.assertText(validator=u'Clicked', id=u'clickme')['result']
    assert client.doubleClick(id=u'dblclickme')['result']
    assert client.asserts.assertText(validator=u'Double Clicked', id=u'dblclickme')['result']
    assert client.mouseDown(id=u'mousedownme')['result']
    assert client.asserts.assertText(validator=u'mouse downed', id=u'mousedownme')['result']
    assert client.mouseUp(id=u'mouseupme')['result']
    assert client.mouseOver(id=u'mouseoverme')['result']
    assert client.asserts.assertText(validator=u'mouse overred',id=u'mouseoverme')['result']
    assert client.mouseOut(id=u'mouseoverme')['result']
    assert client.asserts.assertText(validator=u'mouseouted',id=u'mouseoverme')['result']
    assert client.asserts.assertText(validator=u'mouse upped', id=u'mouseupme')['result']
    assert client.asserts.assertNode(id=u'amIhere')['result']
    assert client.asserts.assertProperty(validator=u'style.height|50px', id=u'amIhere')['result']
    assert not client.asserts.assertNode(id=u'doesntExist')['result']
    assert not client.asserts.assertNode(id=u'created')['result']
    assert client.click(id=u'wfeBtn')['result']
    assert client.waits.forElement(id=u'created', timeout=u'40000')['result']
    assert client.asserts.assertNode(id=u'created')['result']
    assert client.asserts.assertJS(js=u'window.document.title == "windmill_js_unit"')
    assert client.asserts.assertIDEJS(js=u'window.document.title == "Windmill IDE"')
    assert client.execJS(js=u'window.awesome = true;')
    assert client.asserts.assertJS(js=u'window.awesome == true;')
    assert client.execIDEJS(js=u'window.awesome = false;')
    assert client.asserts.assertIDEJS(js=u'window.awesome == false;')