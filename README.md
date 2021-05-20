# Jarvis #

Jarvis is an artificial intelligence program that automates your day-to-day working, just by giving it a command.

## My Jarvis ##

My Jarvis AI can automate the following processes for you:

* Open Google.
* Open websites like YouTube, GitHub and LinkedIn.
* Retrieve wikipedia information.
* Tell you the current time.
* Send emails.
* Play downloaded songs.

## Installations ##

You first need to run these commands in your terminal and install the following modules, if not already present in your PC.

```
pip install pyttsx3
```

```
pip install speechRecognition
```

```
pip install wikipedia
```
## Instructions for Usage ##

### Wikipedia Feature: ###

To use the wikipedia feature, you have to say the name along with the word 'wikipedia' to get your search result. For example, if you want some information about John Doe you have to say 'John Doe wikipedia'.

This feature by default will retrieve three sentence information from the wikipedia page.

```
results=wikipedia.summary(query,sentences=3)
```

Change the value of 'sentences' in Jarvis.py file to get the information accordingly.

### Opening any website in Browser: ###

You can automate the opening of any website, like I have automated Youtube, GitHub and LinkedIn. Just copy the code given below and paste it inside the main function, in Jarvis.py file.

```
elif 'open website_name' in query:
            # This condition runs if 'open github' is in the search query. Uses webbrowser module.
            webbrowser.open("website_name.com")
```

Rewrite the name of the website in place of 'website_name'.
Finally, if you want to open LinkedIn, say 'open LinkedIn'. 

### To know the current time: ###

This feature will tell you the time according to the time which is there in your PCs clock. So make sure your PCs clock is correct. 
To use this feature you just have to say 'Tell me the time'. 

### Send Emails to anyone: ###

Follow the below instructions to automate this function of sending email to anyone:

* You have to enable the 'Allow less secure apps' feature of your gmail account with which you want to send emails to your friends:
Manage your Google Account -> Security -> Less secure app access -> Turn on access -> Turn on 'Allow less secure apps' option.

* In Jarvis.py file, a function 'emaiList()' is defined. Inside that function, there is a statment written as follows:

```
emailDict={"friend1":"friend1email@gmail.com","friend2":"friend2email@gmail.com","friend3":"friend3email@gmail.com","friend4":"friend4email@gmail.com"}
```

Rewrite your friends or colleagues names and their gmail addresses in place of these key-value pairs.
You can write as many names and gmail addresses as you want, inside the emailDict dictionary.

* Now see the 'sendEmail()' function in Jarvis.py file. You need to rewrite your gmail address(the one with allow less secured apps option enabled), wherever 'youremail@gmail.com' is written and save the file.

* The last important step is, you have to write your password in dish.txt file(for security concerns), and save it.

* Finally, you need to command Jarvis to send email to your friend by saying, for example, 'send email to john doe'. Jarvis will ask you 'what should i say', then dictate the whole content of your email.

### Play downloaded songs: ### 
```
elif 'play music' in query:
            # Uses random and os module to randomly choose and play any song listed in your playlist folder. The folder's path should be stored in 'myDir' variable 
            myDir="Enter-your-folder-location-here"
            music=os.listdir(myDir)
            j=0
            for i in music:
                i=random.choice(music)
                if music[j]==i:
                    os.startfile(os.path.join(myDir,music[j]))
                    j=0
                else:
                    j=j+1
```
Copy and paste the above given codes in Jarvis.py file inside the main functin as an elif condition.

* Go to the songs folder in your PC. Copy the location of any one song present inside the folder.

* Paste the location in place of 'Enter-your-location-here' and put double slashes instead of single slashes in between the path. For example, "C:\\\Users\\\Hewlett Packard\\\PycharmProjects\\\Jarvis\\\songs".

* Now to play songs you just have to say 'play songs'.

### Exit Jarvis: ###

To exit the Jarvis program you just have to say 'exit'.

## Contributing ##

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



