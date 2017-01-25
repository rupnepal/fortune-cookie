#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

class MainHandler(webapp2.RequestHandler):
    def getrandomFortune(self):
        fortune=["A smile is your passport into the hearts of others.",
        "Now is the time to try something new.",
        "If winter comes,can spring be far behind?",
        "You will travel to many exotic places in your lifetime.",
        "If there is will there is way."]
        display=random.choice(fortune)
        return display

    def get(self):
        topic="<h1>Fortune Cookie</h1>"

        fortune="<strong>"+self.getrandomFortune()+"</strong>"
        fortune_sentence="your fortune: " + fortune
        fortune_paragraph="<p>" + fortune_sentence +"</p>"

        number="<strong>"+str(random.randint(1,100))+"</strong>"
        num_sentence="your lucky number: "+ number
        num_paragraph="<p>" +num_sentence +"</p>"
        cookie_button="<a href='.'><button>Another Cookie Please</button></a>"

        content=topic +fortune_paragraph+num_paragraph +cookie_button

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
