.mode column
.headers on

SELECT book.title, creator.name
FROM ((bookCreator
INNER JOIN creator
ON bookCreator.creatorId=creator.id)
INNER JOIN book
ON book.id=bookCreator.bookId)
WHERE bookCreator.bookID=4;
