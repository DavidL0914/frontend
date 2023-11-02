import random

quotes_data = []
quote_list = [
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "Success is not final; failure is not fatal: It is the courage to continue that counts.",
    "The future depends on what you do today.",
    "You are never too old to set another goal or to dream a new dream.",
    "In the middle of every difficulty lies opportunity.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "Your time is limited, don't waste it living someone else's life.",
    "The best way to predict the future is to create it.",
]

# Initialize quotes
def initQuotes():
    # Setup quotes into a dictionary with id, text, upvotes, downvotes
    item_id = 0
    for item in quote_list:
        quotes_data.append({"id": item_id, "text": item, "upvotes": 0, "downvotes": 0})
        item_id += 1
    # Prime some upvotes
    for i in range(5):
        id = getRandomQuote()['id']
        upvoteQuote(id)
    # Prime some downvotes
    for i in range(3):
        id = getRandomQuote()['id']
        downvoteQuote(id)

# Return all quotes from quotes_data
def getQuotes():
    return quotes_data

# Quote getter
def getQuote(id):
    return quotes_data[id]

# Return random quote from quotes_data
def getRandomQuote():
    return random.choice(quotes_data)

# Most liked quote
def favoriteQuote():
    best = 0
    bestID = -1
    for quote in getQuotes():
        if quote['upvotes'] > best:
            best = quote['upvotes']
            bestID = quote['id']
    return quotes_data[bestID]

# Most downvoted quote
def jeeredQuote():
    worst = 0
    worstID = -1
    for quote in getQuotes():
        if quote['downvotes'] > worst:
            worst = quote['downvotes']
            worstID = quote['id']
    return quotes_data[worstID]

# Add an upvote for the requested id
def upvoteQuote(id):
    quotes_data[id]['upvotes'] = quotes_data[id]['upvotes'] + 1
    return quotes_data[id]['upvotes']

# Add a downvote for the requested id
def downvoteQuote(id):
    quotes_data[id]['downvotes'] = quotes_data[id]['downvotes'] + 1
    return quotes_data[id]['downvotes']

# Pretty Print quote
def printQuote(quote):
    print(quote['id'], quote['text'], "\n", "Upvotes:", quote['upvotes'], "\n", "Downvotes:", quote['downvotes'], "\n")

# Number of quotes
def countQuotes():
    return len(quotes_data)

# Test Quote Model
if __name__ == "__main__":
    initQuotes()  # Initialize quotes

    # Most liked and most downvoted quotes
    best = favoriteQuote()
    print("Most liked", best['upvotes'])
    printQuote(best)
    worst = jeeredQuote()
    print("Most downvoted", worst['downvotes'])
    printQuote(worst)

    # Random quote
    print("Random quote")
    printQuote(getRandomQuote())

    # Count of Quotes
    print("Quotes Count: " + str(countQuotes()))
