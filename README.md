
# Make your own IDM using python

I'll show you how to create your own Internet Download Manager (IDM) using Python. With just 7 lines of code, you can easily download YouTube videos directly from your Python console. This simple and effective technique is perfect for anyone who wants to streamline their workflow and make the most of their time online.

let's start...............

To make this project you need to follow this step:-










## Installation

Install package with pip

```bash
pip install pytube

```
    
## Deployment

To deploy this project run

```bash
# Please Subscribe my youtube channel "@problemsolvewithridoy"

from pytube import YouTube

url = input("please enter your youtube video link: ")
yt = YouTube(url)

video = yt.streams.filter(progressive= True, file_extension= "mp4").order_by("resolution").desc().first()
video.download()
print("Congratulations, your download is completed")
```

## You can follow me

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

YouTube:- https://www.youtube.com/@problemsolvewithridoy

Gmail:- entridoy2@gmail.com

If you have any confusion, please feel free to contact me. Thank you


## License
This script is released under the MIT License. Feel free to use, modify, and distribute it as you wish. If you find any bugs or have any suggestions for improvement, please submit an issue or a pull request on this repository.

