'''
Description: Exploring my personal carbon footprint and writing a program that gives the users' inputed data and outputs an approximation of their digital footprint, along with a summary of their carbon footprint and some additional information. 
Created By: Shiv Patel
Date Created: 28/02/2022
Date Last Modified: 08/03/2022
'''

blankLine = "\n"

# Introduction to code
print ("Welcome to the Digital Carbon Footprint Approximator! \n\nPlease follow the instructions and enter/input your responses depending on what is being asked for to get the most accurate responses!")
print (blankLine)

# Asking the user to number of days they collected their data
daysCollected = int(input("How many days did you track your data for?: "))
print (blankLine)

# Asking the user the units of their data (Minutes or hours)
minuteUnit = "min"  
hourUnit = "hour" 

dataType = input("Was your data collected in minutes or hours? (If minutes, input 'min'/if hours input 'hour'): ")

if dataType == hourUnit: 

    # Asking the user to input all of their collected data
    textMessage = float(input("How many times did you send a text message over your data collection period?: "))
    phoneCall = float(input("How many hours did you spend calling over your data collection period?: "))
    googleSearch = float(input("How many searches on Google did you make over data collection period?: "))
    sendingEmails = float(input("How many emails did you send over your data collection period?: "))
    tiktokMedia = float(input("How many hours did you spending using TikTok over your data collection period?: "))
    instagramMedia = float(input("How many hours did you spend using Instagram over your data collection period?: "))
    spotifyMusic = float(input("How many hours did you spend listening to music on Spotify over your data collection period?: "))
    youtubeVideos = float(input("How many hours did you spend watching YouTube videos over your data collection period?: "))
    netflixStream = float(input("How many hours did you spend watching Netflix over your data collection period?: "))
    videoGames = float(input("How many hours did you spend playing video games over your data collection period?: "))

    print (blankLine)

    # Asking the user to input a number of days and people to extrapolate to 
    daysExtrapolate = int(input("How many days would you like to extrapolate your data to?: "))
    peopleExtrapolate = int(input("How many peoples would you extrapolate your data to?: "))

    print (blankLine)

    # Calculating the amount of actions they performed, considering a 10% margin error
    print ("*Calculated considering a 10% margin error*: ")
    print (blankLine)

    print ("According to your data, over", daysCollected, "days, you: ")
    textSubtract =  round(textMessage * 0.9, 2) 
    textAdd = round(textMessage * 1.1, 2)
    phoneSubtract = round(phoneCall * 0.9, 2)
    phoneAdd = round(phoneCall * 1.1, 2)
    googleSubtract = round(googleSearch * 0.9, 2)  
    googleAdd = round(googleSearch * 1.1, 2)
    emailSubtract = round(sendingEmails * 0.9, 2) 
    emailAdd = round(sendingEmails * 1.1, 2)
    tiktokSubtract = round(tiktokMedia * 0.9, 2) 
    tiktokAdd = round(tiktokMedia * 1.1, 2)
    instagramSubtract = round(instagramMedia * 0.9, 2) 
    instagramAdd = round(instagramMedia * 1.1, 2)
    spotifySubtract = round(spotifyMusic * 0.9, 2)
    spotifyAdd = round(spotifyMusic * 1.1, 2)
    youtubeSubtract = round(netflixStream * 0.9, 2)  
    youtubeAdd = round(netflixStream * 0.9, 2)  
    netflixSubtract = round(netflixStream * 1.1, 2)
    netflixAdd = round(netflixStream * 1.1, 2)
    gamingSubtract = round(videoGames * 0.9, 2) 
    gamingAdd =  round(videoGames * 1.1, 2)
    print (blankLine)

    print ("Sent", textSubtract, "to", textAdd, "text messages!")
    print("Made", phoneSubtract, "to", phoneAdd, "phone calls!")
    print ("Made", googleSubtract, "to", googleAdd, "searches on Google!")
    print ("Sent", emailSubtract, "to", emailAdd, "emails!")
    print ("Watched", tiktokSubtract, "to", tiktokAdd, "hours of TikTok!")
    print ("Scrolled", instagramSubtract, "to", instagramAdd, "hours on Instagram!")
    print ("Listened to", spotifySubtract, "to", spotifyAdd, "hours of Spotify!")
    print ("Watched", youtubeSubtract, "to", youtubeAdd, "hours of YouTube!")
    print ("Watched", netflixSubtract, "to", netflixAdd, "hours of Netflix!")
    print ("Played", gamingSubtract, "to", gamingAdd, "hours of video games!")

    print (blankLine)

    # The amount of carbon dioxide emissions generated in the number of days they collected their data 
    textCarbon = textSubtract * 0.014
    phoneCarbon = phoneSubtract * 6
    googleCarbon = googleSubtract * 0.2
    emailCarbon = emailSubtract * 4
    tiktokCarbon = tiktokSubtract * 157.8
    instagramCarbon = instagramSubtract * 63
    spotifyCarbon = spotifySubtract * 55
    youtubeCarbon = youtubeSubtract * 27.6
    netflixCarbon = netflixSubtract * 36
    gamingCarbon = gamingSubtract * 55.02

    totalCarbon = round(textCarbon + phoneCarbon + googleCarbon + emailCarbon + tiktokCarbon +        instagramCarbon + spotifyCarbon + youtubeCarbon + netflixCarbon + gamingCarbon, 2)

    textEmissions = textAdd * 0.014
    phoneEmissions = phoneAdd * 6
    googleEmissions = googleAdd * 0.2
    emailEmissions = emailAdd * 4
    tiktokEmissions = tiktokAdd * 157.8
    instagramEmissions = instagramAdd * 63
    spotifyEmissions = spotifyAdd * 55
    youtubeEmissions = youtubeAdd * 27.6
    netflixEmissions = netflixAdd * 36
    gamingEmissions = gamingAdd * 55.02

    carbonEmissions = round(textEmissions + phoneEmissions + googleEmissions + emailEmissions + tiktokEmissions + instagramEmissions + spotifyEmissions + youtubeEmissions + netflixEmissions + gamingEmissions, 2) 

    print ("You have generated around", totalCarbon, "-", carbonEmissions, "g of CO2 emissions in", daysCollected, "days.")
    print (blankLine)

    # The amount of carbon dioxide emissions that would be generated in extrapolated days scenario 
    extrapolatedCarbon = round((totalCarbon / daysCollected) * daysExtrapolate, 2)
    extrapolatedEmissions = round((carbonEmissions/daysCollected) * daysExtrapolate, 2)
    print ("Considering your current rate of CO2 emissions, in", daysExtrapolate, "days you would emit", extrapolatedCarbon, "-", extrapolatedEmissions, "g of CO2.")
    print (blankLine)

    # The amount of carbon dioxide emissions that would be generated in the extrapolated days and the extrapolated number of people scenario
    extrapolatedCarbon = round (extrapolatedCarbon * peopleExtrapolate, 2)
    extrapolatedEmissions = round(extrapolatedEmissions * peopleExtrapolate, 2)
    print ("If", peopleExtrapolate, "people followed your CO2 emission patterns, in", daysExtrapolate, "days,", peopleExtrapolate, "people would emit", extrapolatedCarbon, "-", extrapolatedEmissions, "g of CO2.")
    print (blankLine)

    # The amount of money that should be spent to on carbon offsets to balance the carbon footprint in the extrapolated data scenario 
    print ("Here are 3 carbon offsetting projects that are available in Canada or around the world: ")
    print ("1. Essex-Windsor Regional Landfill Gas Capture and Destruction")
    print ("2. Planetair+Canada (Reforestation)")
    print ("3. Afognak Forest Carbon Project")
    print (blankLine)

    offsetChoice = int(input("Please enter either 1, 2, or 3, calling the carbon offset project you would like to explore: "))

    # Carbon offset choice #1: Vietnam Municipal Solid Waste Treatment (converts grams of CO2 emissions to tonnes, as offsets are measured in $/tonne)
    if offsetChoice == 1: 
        vietOffset = round((extrapolatedCarbon / 1000000) * 24, 2)
        vietCarbon = round((extrapolatedEmissions / 1000000) * 24, 2)
        print ("The 'Vietstar Municipal Solid Waste Treatment Plant in Vietnam', a Gold Standard carbon offset option based in Canada costs $24 CAD/tonne. If you chose this option as a carbon offset, $" +str(vietOffset), "- $" + str(vietCarbon), "would need to be spent to offset",       peopleExtrapolate, "indivduals carbon emissions over", daysExtrapolate, "days.")

    # Carbon offset choice #2: Reforestation in Canada (converts grams of CO2 emissions to tonnes, as offsets are measured in $/tonne)
    if offsetChoice == 2: 
        planetOffset = round((extrapolatedCarbon / 1000000) * 32, 2)
        planetCarbon = round((extrapolatedEmissions / 1000000) * 32, 2)
        print ("The 'Plantain (Reforestation) in Canada', a Gold Standard carbon offset option based in Canada costs $32 CAD/tonne. If you chose this option as a carbon offset, $" +str(planetOffset), "- $" + str(planetCarbon), "would need to be spent to offset", peopleExtrapolate, "indivduals carbon emissions over", daysExtrapolate, "days.")

    # Carbon offset choice # 3: Afognak Forest Project in Alaska (converts grams of CO2 emissions to tonnes, as offsets are measured in $/tonne)
    if offsetChoice == 3:
        afcognakOffset = round((extrapolatedCarbon / 1000000) * 30, 2)
        afcognakCarbon = round((extrapolatedEmissions / 1000000) * 30, 2)
        print ("Afognak Forest Carbon Project', a Gold Standard carbon offset option based in Alaska, costs $30 CAD/tonne. If you chose this option as a carbon offset, $" +str(afcognakOffset), "- $" + str(afcognakCarbon), "would need to be spent to offset", peopleExtrapolate, "indivduals carbon emissions over", daysExtrapolate, "days.")

    if offsetChoice > 3 or offsetChoice <= 0:
        print ("Please try again. ")

elif dataType == minuteUnit: 
    # Asking the user to input all of their collected data
    textMessage = int(input("How many times did you send a text message over your data collection period?: "))
    phoneCall = int(input("How many minutes did you spend calling over your data collection period?: "))
    googleSearch = int(input("How many searches on Google did you make over data collection period?: "))
    sendingEmails = int(input("How many emails did you send over your data collection period?: "))
    tiktokMedia = int(input("How many minutes did you spending using TikTok over your data collection period?: "))
    instagramMedia = int(input("How many minutes did you spend using Instagram over your data collection period?: "))
    spotifyMusic = int(input("How many minutes did you spend listening to music on Spotify over your data collection period?: "))
    youtubeVideos = int(input("How many minutes did you spend watching YouTube videos over your data collection period?: "))
    netflixStream = int(input("How many minutes did you spend watching Netflix over your data collection period?: "))
    videoGames = int(input("How many minutes did you spend playing video games over your data collection period?: "))

    print (blankLine)

    # Asking the user to input a number of days and people to extrapolate to 
    daysExtrapolate = int(input("How many days would you like to extrapolate your data to?: "))
    peopleExtrapolate = int(input("How many peoples would you extrapolate your data to?: "))

    print (blankLine)

    # Calculating the amount of actions they performed, considering a 10% margin error
    print ("*Calculated considering a 10% margin error*: ")

    print (blankLine)

    print ("According to your data, over", daysCollected, "days, you: ")
    textSubtract =  round(textMessage * 0.9) 
    textAdd = round(textMessage * 1.1)
    phoneSubtract = round(phoneCall * 0.9)
    phoneAdd = round(phoneCall * 1.1)
    googleSubtract = round(googleSearch * 0.9)  
    googleAdd = round(googleSearch * 1.1)
    emailSubtract = round(sendingEmails * 0.9) 
    emailAdd = round(sendingEmails * 1.1)
    tiktokSubtract = round(tiktokMedia * 0.9) 
    tiktokAdd = round(tiktokMedia * 1.1)
    instagramSubtract = round(instagramMedia * 0.9) 
    instagramAdd = round(instagramMedia * 1.1)
    spotifySubtract = round(spotifyMusic * 0.9)
    spotifyAdd = round(spotifyMusic * 1.1)
    youtubeSubtract = round(youtubeVideos * 0.9)  
    youtubeAdd = round(youtubeVideos * 1.1)
    netflixSubtract = round(netflixStream * 0.9)  
    netflixAdd = round(netflixStream * 1.1)
    gamingSubtract = round(videoGames * 0.9) 
    gamingAdd = round(videoGames * 1.1)
    print (blankLine)

    print ("Sent", textSubtract, "to", textAdd, "text messages!")
    print("Made", phoneSubtract, "to", phoneAdd, "phone calls!")
    print ("Made", googleSubtract, "to", googleAdd, "searches on Google!")
    print ("Sent", emailSubtract, "to", emailAdd, "emails!")
    print ("Watched", tiktokSubtract, "to", tiktokAdd, "minutes of TikTok!")
    print ("Scrolled", instagramSubtract, "to", instagramAdd, "minutes on Instagram!")
    print ("Listened to", spotifySubtract, "to", spotifyAdd, "minutes of Spotify!")
    print ("Watched", youtubeSubtract, "to", youtubeAdd, "minutes of YouTube!")
    print ("Watched", netflixSubtract, "to", netflixAdd, "minutes of Netflix!")
    print ("Played", gamingSubtract, "to", gamingAdd, "minutes of video games!")
    
    print (blankLine)

    # The amount of carbon dioxide emissions generated in the number of days they collected their data 
    textCarbon = textSubtract * 0.014
    phoneCarbon = phoneSubtract * 0.1
    googleCarbon = googleSubtract * 0.2
    emailCarbon = emailSubtract * 4
    tiktokCarbon = tiktokSubtract * 2.63
    instagramCarbon = instagramSubtract * 1.05
    spotifyCarbon = spotifySubtract * 0.91
    youtubeCarbon = youtubeSubtract * 0.46
    netflixCarbon = netflixSubtract * 0.6
    gamingCarbon = gamingSubtract * 0.917

    totalCarbon = round(textCarbon + phoneCarbon + googleCarbon + emailCarbon + tiktokCarbon + instagramCarbon + spotifyCarbon + youtubeCarbon + netflixCarbon + gamingCarbon, 2)

    textEmissions = textAdd * 0.014
    phoneEmissions = phoneAdd * 0.1
    googleEmissions = googleAdd * 0.2
    emailEmissions = emailAdd * 4
    tiktokEmissions = tiktokAdd * 2.63
    instagramEmissions = instagramAdd * 1.05
    spotifyEmissions = spotifyAdd * 0.91
    youtubeEmissions = youtubeAdd * 0.46
    netflixEmissions = netflixAdd * 0.6
    gamingEmissions = gamingAdd * 0.917

    carbonEmissions = round(textEmissions + phoneEmissions + googleEmissions + emailEmissions + tiktokEmissions + instagramEmissions + spotifyEmissions + youtubeEmissions + netflixEmissions + gamingEmissions, 2) 

    print ("You have generated around", totalCarbon, "-", carbonEmissions, "g of CO2 emissions in", daysCollected, "days.")
    print (blankLine)

    # The amount of carbon dioxide emissions that would be generated in extrapolated days scenario 
    extrapolatedCarbon = round((totalCarbon / daysCollected) * daysExtrapolate, 2)
    extrapolatedEmissions = round((carbonEmissions/daysCollected) * daysExtrapolate, 2)
    print ("Considering your current rate of CO2 emissions, in", daysExtrapolate, "days you would emit", extrapolatedCarbon, "-", extrapolatedEmissions, "g of CO2.")
    print (blankLine)

    # The amount of carbon dioxide emissions that would be generated in the extrapolated days and the extrapolated number of people scenario
    extrapolatedCarbon = round (extrapolatedCarbon * peopleExtrapolate, 2)
    extrapolatedEmissions = round(extrapolatedEmissions * peopleExtrapolate, 2)
    print ("If", peopleExtrapolate, "people followed your CO2 emission patterns, in", daysExtrapolate, "days,", peopleExtrapolate, "people would emit", extrapolatedCarbon, "-", extrapolatedEmissions, "g of CO2.")
    print (blankLine)

    # The amount of money that should be spent to on carbon offsets to balance the carbon footprint in the extrapolated data scenario 
    print ("Here are 3 carbon offsetting projects that are available in Canada or around the world: ")
    print ("1. Essex-Windsor Regional Landfill Gas Capture and Destruction")
    print ("2. Planetair+Canada (Reforestation)")
    print ("3. Afognak Forest Carbon Project")
    print (blankLine)

    offsetChoice = int(input("Please enter either 1, 2, or 3, calling the carbon offset project you would like to explore: "))

    print (blankLine)
    # Carbon offset choice #1: Vietnam Municipal Solid Waste Treatment (converts grams of CO2 emissions to tonnes, as offsets are measured in $/tonne)
    if offsetChoice == 1: 
        vietOffset = round((extrapolatedCarbon / 1000000) * 24, 2)
        vietCarbon = round((extrapolatedEmissions / 1000000) * 24, 2)
        print ("The 'Vietstar Municipal Solid Waste Treatment Plant in Vietnam', a Gold Standard carbon offset option based in Canada costs $24 CAD/tonne. If you chose this option as a carbon offset, $" +str(vietOffset), "- $" + str(vietCarbon), "would need to be spent to offset",       peopleExtrapolate, "indivduals carbon emissions over", daysExtrapolate, "days.")

    # Carbon offset choice #2: Reforestation in Canada (converts grams of CO2 emissions to tonnes, as offsets are measured in $/tonne)
    if offsetChoice == 2: 
        planetOffset = round((extrapolatedCarbon / 1000000) * 32, 2)
        planetCarbon = round((extrapolatedEmissions / 1000000) * 32, 2)
        print ("The 'Plantair (Reforestation) in Canada', a Gold Standard carbon offset option based in Canada costs $32 CAD/tonne. If you chose this option as a carbon offset, $" +str(planetOffset), "- $" + str(planetCarbon), "would need to be spent to offset", peopleExtrapolate, "indivduals carbon emissions over", daysExtrapolate, "days.")

    # Carbon offset choice # 3: Afognak Forest Project in Alaska (converts grams of CO2 emissions to tonnes, as offsets are measured in $/tonne)
    if offsetChoice == 3:
        afcognakOffset = round((extrapolatedCarbon / 1000000) * 30, 2)
        afcognakCarbon = round((extrapolatedEmissions / 1000000) * 30, 2)
        print ("Afognak Forest Carbon Project', a Gold Standard carbon offset option based in Alaska, costs $30 CAD/tonne. If you chose this option as a carbon offset, $" +str(afcognakOffset), "- $" + str(afcognakCarbon), "would need to be spent to offset", peopleExtrapolate, "indivduals carbon emissions over", daysExtrapolate, "days.")

    if offsetChoice > 3 or offsetChoice <= 0:
        print ("Please try again. ")

else: 
    print (blankLine)
    print ("Invalid unit input. Please try again. \n(If you entered the correct unit, please try entering only 'min' without additional characters and/or spaces.")
print (blankLine)

print ("Thank you for using the Digital Footprint Approximator! \nHopefully you have understood the impacts your virtual actions are making on the environment, even though the media may say otherwise.")
print (blankLine)

# Providing the user with some tips to reduce their carbon footprint
tipsChoice = input("Would you like some effective tips on how you could reduce your carbon footprint and/or carbon emissions? (only 'yes' or 'no'): ")
print (blankLine)
if tipsChoice == "yes": 
    print ("- Deleted old emails from your mailbox that you don't need.") 
    print ("- Unsubscribe from any promitional offers or newsletter that you don't require or use anymore.") 
    print ("-When possible, reduce video or streaming settings before watching videos.") 
    print ("- Unplug or power off devices when not in use.")
    
else: 
    print ("Thank you. Have a great day!")
print (blankLine)

# ASCII art

print (
"     __   _"                     "               __   _"                        
"\n    (  )_( )_"                 "            (  )_( )_"                
"\n   (_   _    _)"               "        (_   _    _)"
"\n     (_) (__)"                 "            (_) (__)")


print ("\n")

print (

"      ______"                  "                ______" 
"\n     /|_||_\`.__"            "           /|_||_\`.__"
"\n    (   _    _ _\ "          "        (   _    _ _\ "
"\n  ===`-(_)--(_)-"            "        ===`-(_)--(_)-"
)

print (" ---------------------------------------------------")
