import pytube

def youtube_mp4(link_supplied):

    #Location where the downloaded vides will be stored
    storage_path = "Youtube videos"     
    '''This will automatically generates a folder named "Youtube videos for the first download. 
    Susequent downloaded videos will be stored in this file
    
    '''

    pytube.YouTube(link_supplied).streams.get_highest_resolution().download(storage_path)