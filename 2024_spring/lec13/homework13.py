import bs4, gtts

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.
    
    @params: 
    text (string): the text of a webpage
    
    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    #raise RuntimeError('You need to write this part!')
    soup = bs4.BeautifulSoup(text, 'html.parser')
    stories = []
    story_elements = soup.find_all('div', class_='story')
    for element in story_elements:
        # Extract title
        title_tag = element.find('h3', class_='title')
        if title_tag:
            title = title_tag.text.strip()
        else:
            continue
        teaser_tag = element.find('p', class_='teaser')
        if teaser_tag:
            teaser = teaser_tag.text.strip()
        else:
            teaser = ''
        stories.append((title, teaser))  
    return stories
    
def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.
    
    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio


    Output: None
    '''
    #raise RuntimeError('You need to write this part!')
    if n < 0 or n >= len(stories):
        raise IndexError('Invalid story index')
    title, teaser = stories[n]
    full_text = f'{title}. {teaser}'
    tts = gTTS(full_text, lang='en')
    tts.save(filename)
    print(f'Story {n+1} has been synthesized and saved as {filename}')
