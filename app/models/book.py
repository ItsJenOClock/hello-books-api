class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
    
books = [
    Book(1, "Blade Runner", "A sci-fi novel set in a dystopian Los Angeles."),
    Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
    Book(3, "It", "A horror novel set in a small town.")
]
