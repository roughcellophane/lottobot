import random
import facebook
import pdfcrowd
import sys
import datetime
import time

#function defining
def chkr1(a, b, c, d):
    while len(d) != 6:
        cntrNew = 0
        while cntrNew < (b - c):
            num = random.randint(1, 58)
            if num not in d:
                if len(d) == b:
                    break
                else:
                    d.add(num)
            cntrNew += 1
            chkr2(a, b, c, d)

def chkr2(a, b, c, d):
    if b != len(d):
        chkr1(a, b, c, d)
        
###################         CODE PART           ###################

while True:
    if datetime.datetime.now().minute % 15 == 0:
        #First Assignment
        draws = []
        cntr = 0
        while cntr < 6:
            num = random.randint(1, 58)
            draws.append(num)
            cntr += 1
        #Complicated Part: Finalization of Numbers (just in case repetition of numbers occur)
        drawsSetMain = set(draws)  #d
        drawsSet = set(draws)      #a
        drawCount = len(draws)     #b
        setCount = len(drawsSet)   #c

        chkr2(drawsSet, drawCount, setCount, drawsSetMain)
        finalDraws = list(drawsSetMain)
        finalNumbers = str(str(finalDraws[0]) + "      " + str(finalDraws[1]) + "      " + str(finalDraws[2]) + "      " + str(finalDraws[3]) + "      " + str(finalDraws[4]) + "      " + str(finalDraws[5]))
        prtMsg = "Numbers:  \n" + finalNumbers
        #Making HTML File
        htmlContent="""
        <html>
        <head>
        <style>
        body{
        	font-family: Helvetica;
            text-align: center;
            color: #23395d
            }
        #header{
            font-size: 60px;
            }
        #nums{
            font-size: 48px;
            font-family: Helvetica;
	}
        </style>
        </head>
        <body>
        <p id="header">LottoBot</p>
        <pre id="nums">Numbers:<br>""" + finalNumbers
        
        
        
        html_file = open("picTransform.html", "w")
        html_file.write(htmlContent)
        html_file.close()

        #HTML Conversion to PNG by PdfCrowd
        try:
            # create the API client instance
            client = pdfcrowd.HtmlToImageClient('cellopha_ne', '9246f4e37aaffcee2dd2ab6d6a9e0f27')
        
            # configure the conversion
            client.setOutputFormat('png')
        
           # create output file for conversion result
            output_file = open('numbers.png', 'wb')

            # run the conversion and store the result into an image variable
            image = client.convertFile('picTransform.html')

            # write the image into the output file
            output_file.write(image)

            # close the output file
            output_file.close()
        except pdfcrowd.Error as why:
        # report the error
            sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

        # handle the exception here or rethrow and handle it at a higher level
            raise

        #Posting in Facebook
        graph = facebook.GraphAPI(timeout=3600, access_token="EAACVS6jUj0QBAGE1LiZBYO77j2ZB05jU99I6Ijpox4cygZCZBWm4ZAu3RYEbeE0eRZCqmw5WnxcNvFLbCxrZBwCw4SjgCoZBysYu1o3dbHtVyR9Y3zC0SGuMjaY9v3AwE5CBF7uCWa6bTR5B0IpZCC0zJTZAZBS4YzRViVzDCMSDBekogZDZD", version="2.12")
        graph.put_photo(image=open("numbers.png", 'rb'), album_path="/me/photos" + "/picture")
        #graph.put_object(parent_object='me', connection_name='feed', message='Good morning!')
        
        
        #Number Printing
        print(prtMsg)
    time.sleep(60)

