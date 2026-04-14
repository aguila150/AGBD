SELECT FirstName, LastName FROM employees 
ORDER by FirstName ASC

SELECT name, Milliseconds FROM tracks 
JOIN albums ON tracks.AlbumId = albums.AlbumId
WHERE albums.Title LIKE 'Big Ones' 
ORDER by tracks.Milliseconds DESC

SELECT name, UnitPrice FROM tracks
ORDER by UnitPrice ASC LIMIT 10

SELECT t.name, g.name AS Genre, a.Title FROM tracks t
JOIN albums a ON t.AlbumId = a.AlbumId 
JOIN genres g ON t.GenreId = g.GenreId
WHERE t.UnitPrice = 0.99

SELECT t.name, t.Milliseconds, a.Title, art.name AS Artista  FROM tracks t
JOIN albums a ON t.AlbumId = a.AlbumId 
JOIN genres g ON t.GenreId = g.GenreId
JOIN artists art ON a.ArtistId = art.ArtistId
ORDER by t.Milliseconds ASC LIMIT 20

SELECT emp.LastName AS empleado, jefe.LastName AS jefe, COUNT(*)  FROM employees emp
JOIN employees jefe ON emp.ReportsTo = jefe.EmployeeId
JOIN customers cus ON emp.EmployeeId = cus.SupportRepId
GROUP BY emp.EmployeeId
ORDER by jefe ASC