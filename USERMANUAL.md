DefAI “How-to” User Manual 

Table of Contents 

Introduction 

Installation 

Setup 

Usage 

Tips and Tricks 

 

Introduction 

What is DefAI? 

DefAI is a downloadable software that serves as a “digital cyber assistant” for a user. It is comprised of an AI-language model, the Ai-assistant tool known as Fabric, and code created by the Sphinx Security team to link both together, and other things we added.  

What can DefAI do? 

DefAI can do several different things. It can serve as a general cybersecurity AI, provide valuable insight regarding inputs, analyze captured network traffic for anomalies, provide suggestions on how to improve a network, and more! DefAI v1.0.0 is relatively basic, but its functionality can be expanded in future releases or forked by anyone outside of the Sphinx Security team. 

How does DefAI work? 

DefAI functions by launching an application window for the software, providing users multiple buttons to click that each serve a different function. Clicking a button will launch a designated window with DefAI. Each button will cause DefAI to perform exclusively the task programmed for that button. All users will need to do from there is enter their input (plaintext or a file) and watch DefAI generate a response! 

Where does the “AI” part come in? 

The AI part comes in when you type and send something to the program. It is just an AI language model like OpenAI’s ChatGPT, Google’s Gemini, Microsoft Copilot, DeepSeek, etc. that is receiving your submission and generating the response. What makes it different than just using the service standalone is that we have trained this specific ChatGPT model with extremely specific instructions (called “patterns,” details below) and response guidelines for our specific cyber-related tasks.  

What is Fabric? 

Fabric is an open-source software that serves the purpose of improving the efficiency and response quality of AI LLMs. It does this by using files called “patterns” that are essentially a very specific set of instructions for an LLM to follow. (More info bellow in “Usage”) 

 

Installation 

Where to download? 

DefAI can be downloaded from the associated GitHub page. Simply navigate to the “Releases” tab and download the latest release (v1.0.0) 

How to install? 

To start, extract the contents of the zip file to a convenient location on your device. Inside the extracted file, you should find a folder / various files. Two documents, the User Manual and Readme, will be there. The User Manual is the exact same as the GitHub page instructions. The Readme contains important information, disclaimers, and more detailed instructions. 

But to install DefAI, double click or run the DefAI.exe file. You should get an administrator prompt to run the installer. Hit yes, and then follow the setup-wizards’ instructions as it will install everything you need. Once it finishes, you are good to go! 

Do install locations matter for either DefAI or Fabric? 

Not necessarily. If you install things in a good location you will remember, or the default location we provide, there should be no issues.  

Setup 

Knowing where your installation is 

The default location for DefAI is your “Program files” folder. Within that folder, a folder titled DefAI will be found. Inside the DefAI folder, everything needed will be in there. Alternatively, you can right click on the created desktop shortcut / start menu shortcut and select “Open file location.” 

*Note that this only applies if you kept the default install location, which we recommend to achieve the best functionality and reduce potential errors.  

 

Usage 

What are patterns? 

Patterns are what Fabric takes as part of its input. They essentially are a very specific set of instructions that have been tested through trial and error to produce the best possible response from Fabric. Most patterns function without any additional input, but to get the most tailored and detailed response for a question or task it is recommended to add extra inputs after the pattern is called.  

What patterns does DefAI offer? 

DefAI offers several patterns made by the Sphinx Security team. These include network analysis, General Cyber-related assistance, network vulnerability analysis, behavior analysis, and system vulnerability analysis. 

Can I add my own patterns to DefAI? 

Yes and no. You CAN run other patterns on DefAI, but DefAI itself is not configured properly to print out or accept input from patterns that we did not prepare ourselves. You can do what you wish, but we are once again not liable for any damages to your system or network because of your actions. As well as any legal trouble. You accept that any custom patterns you add are tied to you and you only.  

Can DefAI be run without Fabric / Python installed? 

No. DefAI is dependent on both to function as we intend it to. You may be able to get away without having python itself installed and just use the portable version included with DefAI, but we recommend installing python properly for best performance. 

Tips, Tricks, and Troubleshooting 

Best ways to use DefAI 

It is very self-explanatory! Just mess around with DefAI and see what it can do. The possibilities are endless (so long as they fall under the cybersecurity umbrella we provided) 

How to get the most out of DefAI 

Simply using our provided patterns! We have done the best we can to ensure they are of quality and are perfectly functional. But as with any software, bugs can and do pop up.  

My input outputted a bunch of random gibberish! 

That is merely a side-effect of Fabric and Ollama working together. The technology is still relatively new, and Fabric is in its infancy. The issue can be solved by simply retrying the input you previously tried. If that doesn’t work, try restarting DefAI.  

My input doesn’t return anything! 

This can also happen. Sometimes the output gets lost, it can happen more after DefAI has been running for a long period of time and device resources get used up. Restarting DefAI, or your device, are the best options  

I’m lost / I want to learn more / *insert random other statement here* 

Here are some places you can find out more information! 

Fabric 

 