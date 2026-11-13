authors: Kennedy Richard S. Guerra
author-urls: https://kennedyrichard.com
keywords: GUI
          GUIFT
          stand-in widgets
          approach
description: Essay on a new proposed approach to graphical user interfaces (GUIs) called GUIFT or stand-in widgets
publish-date: 2026-11-16
include-comment-section: True


# Proposing a new approach to graphical user interfaces (GUIs) called GUIFT/stand-in widgets

I think it is safe to assume most PC users nowadays interact with their machines via graphical user interfaces (GUIs). It is no surprise, since they offer at least the benefits listed below (when well-managed, of course):

1. Good sensible layout of elements
1. Widgets that offer efficient and versatile manipulation of values via keyboard and mouse, sometimes other peripherals
1. More rich graphics than usually provided by terminals and other text-based interfaces

Although they emulate GUIs by using the terminal capabilities, other interfaces like TUIs (terminal user interfaces) offer similar benefits as well, with the exception, of course, of rich/detailed graphics, since they depend on the terminal display capabilities.

Even so, the benefits remain roughly the same in varying degrees that ultimately depend on each case. Nonetheless, the capability is there for all of those interfaces. Specially and most importantly regarding the two first benefits listed: layout and versatile widgets.

However, for software developers, all those benefits come with an extra crucial cost: developing and maintaining a graphical user interface (regardless of whether we are using GUIs, TUIs or other similar tools) is time-consuming at best, even when the developer knows what they are doing. At worst, it may result in an unmaintainable mess. GUI code is not exactly know for being well-designed and tidy.

That's why I'd like to propose a new alternative approach to how we usually develop and manage GUIs/TUIs/other similar interfaces. This approach is neither fundamentally better nor worse, but in some cases it may offer vastly superior benefits. Moreover, being an approach, it is not tied to any specific tool/language/paradigm/platform.

In the next sections I present this new alternative approach followed by a use-case.


## Graphical user interfaces from text (GUIFT) or Stand-in widgets


### Presenting the concept

GUIFT (pronounced just like GUI but with the addition of "ft", pronounced like the "ft" in "gift") stands for graphical user interface from text. In other words, this approach consists in the construction of a GUI interface based off of text. It can be prose, code, data, etc., as long as it is text.

Although under the hood text is a unidimensional stream of characters, including the line breaks, which are used to divide this stream further into lines, depending on the text in question, since the line breaks help distribute such stream into 02 dimensions, we already start with a 2D layout. Furthermore, depending on the structure and contents of the text, such layout can be rather elegant.

For instance, take Python code that follows the PEP8 design document. According to such document,

> Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants. ([PEP8](https://peps.python.org/pep-0008/#imports))

Just like import statements, many other elements have their place and formatting defined on that design document, resulting in a text document (the Python module) where each or at least most elements are well laid out and can be properly display in a 2D interface, like in text editors and IDEs (integrated development environments).

There's more about it: text editors, IDEs and other tools like IMEs (input method editors, used to insert special characters like those of CJK and other languages) are able to provide extra functionality by laying out extra visual elements near the text.

For instance, text editor and IDEs may offer different alternatives for auto-completion near the text you are typing and IMEs may offer different text candidates based on the keys you have types so far on your keyboard.

This mean that, in a sense, even though the typing area of text editors and IDEs is reserved for inserting text, the deployment of other visual elements is already performed within the text itself.

Other software applications offer similar capabilities, like spreadsheets. They also offer an interface where the user can insert text, but that same interface is used to transform that text and generate other visual elements like graphs (pie charts, histograms, etc.). Also, they are made for the edition of tabular and numeric data rather than text per se.

GUIFT is just an extension and more intensive exploration of such capability for text in general, regardless of whether it represents prose, code, numbers, values, etc. They this capability is explored is via what I call stand-in widgets. Stand-in widgets are just widgets that stand-in for excerpts of the underlying text, that is, they act as replacements or proxies for that text, holding that text and offering means for its edition. As we just said, such excerpts could represent any kind of text: prose, numeric values, etc.

That's why you can call this approach both GUIFT (its name) or stand-in widgets (the means by which it attains its purpose).


### Exploring the possibilities

In the GUIFT/stand-in widgets approach the edited contents double up as both the input, output and interface of such systems. This means each piece of text (for instance, a text document representing JSON data) already double up as its own GUI. It is as though each text document is already its own app without any extra effort from the user or developer to design and maintain a specific layout. Once the developer creates the individual widgets and services that manage them, each text document builds up its own interface using the stand-in widgets as though they were [Lego](https://en.wikipedia.org/wiki/Lego) pieces.

In the case of a JSON file, regardless of its actual contents, it can be pretty-formatted, making it even easier to display its contents in a 2D text-based interface with a readable and convenient layout. You could then replace some of its values with widgets specialized for editing that kind of value. For instance: an entry specialized for numeric values could replace numbers and a checkbox could replace boolean values.

And just like that, each JSON file is its own GUI.

However, there other problematic aspects to consider. For instance, it is not enough to automatically replace values. Some values only have meaning as elements of a set. For instance, in JSON, the array `(1.0, 1.0, 1.0)` could represent a color or a position in 3D space, so replacing the 03 numbers by an 03 entries would be wrong. Instead, they should be replace by a widget that allows the user to select a color. Furthermore, just because every value or set of values in a JSON file can be replace, it doesn't mean it is of interest to the user. Perhaps the file is very large, with many lines and values and the user only wants to edit a small part of that file. In such case, loading all the possible widgets would be a waste of memory and potentially slow down the editing session.

Because of that, applications using the GUIFT/stand-in widgets approach should be more flexible by allowing users to provide hints regarding which widgets to use and which excerpts those widgets should stand-in for. It might even be possible to be more versatile to allow multiple widgets to manage the same excerpt, for extra functionality. For instance, you could have an entry widget to edit numeric values and another button widget that generates a random numeric value, both managing the same value. This way when the user wants to type a value on purpose it could use the entry and when that same user wants to experiment with random values they could use the button to produce a random value instead.

As GUIFT/stand-in widget is just an approach and not tied to languages, paradigms, platforms, tools, etc., how that is done is left for the developer to decide.

I'll just end up this section with some extra pieces of advice that I think would help the implementation.

First, for the hints provided by users, make it as simple as possible and as non-disruptive as possible for the contents of the text in question. For instance, as well see in a section further ahead, I developed a GUIFT/Stand-in widget software to edit GLSL code (shader code) and I use comments as hints specifying which widgets to use. Since comments in GLSL code are ignored, such hints are non-disruptive to the normal usage of that text.

For text formats that don't include comments, like JSON, you have to be creative and devise alternative ways to provide such hints. For instance, you can require the user to define JSON objects with `"widget-hint"` and `"value"` fields wherever the user want a widget to represent a value.

The second advice is to actually avoid guessing which widgets to use. It is fine to have a mode where the app can guess, but I advise against making this the default setting. Instead, demand that users request the widgets they want and where they want to deploy them in the text via comments, or at least encourage it. The reason for that is that, like I said previously, some values/excerpts only make sense in conjunction with other values and replacing all possible excerpts with widgets could be needlessly resource-intensive.

In programming, I believe it is best to avoid assuming you'll guess right. Instead, focus on providing what the user requests.


### Summary

In summary, the GUIFT/stand-in widgets approach allow developers to provide GUI interfaces to their users without the need to manage as much GUI code.

No need to design and manage different layouts for constantly evolving graphical interfaces. Instead, GUIFT/stand-in widgets differ from other approaches in that the developer only care to build 02 sets of components/features (and their underlying subsystems, of course):

- the widgets themselves
- laying out the text and the requested widgets as defined by the users


## Use-case: Panda3D Stand-in Widget Shader Interface (p3dswshi)

Now let's explore a real published piece of software called p3dswshi (pronounced p-three-d sushi, stands for Panda3D stand-in widget shader interface), which employs the GUIFT/stand-in widget approach.

<!-- 

### TODO

Finish writing section

-->


## Final words

As explored here, once you develop a good base of widgets and the underlying services to manage them and lay them in a 2D interface according to hints provided by users, you'll have a powerful and flexible application that follows the GUIFT/stand-in widgets approach.

It will be as though every piece of text that your app can load and edit works as its own distinct application. Instead of delivering GUI software whose geometry/layout/GUI subsystems you'll have to maintain indefinitely, you'll only have to focus on working on the individual pieces (widgets) that make it up and let your users take advantage of your app to instantly lay out 2D interfaces to edit their text just like they are putting Lego pieces together.

More importantly, there'll be no need for GUI programming for your users to be able to access a custom GUI built for their needs with the requested widgets.

If you found this essay interesting and want to help support my work as an open-source maintainer, you can find me on [Patreon](https://patreon.com/KennedyRichard), GitHub [sponsors](https://github.com/sponsors/KennedyRichard) and other websites like those that you can find on [https://indiesmiths.com/donate](https://indiesmiths.com/donate).

