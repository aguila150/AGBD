1)SELECT FirstName, LastName FROM employees 
  ORDER by FirstName ASC

2)SELECT name, Milliseconds FROM tracks 
  JOIN albums ON tracks.AlbumId = albums.AlbumId
  WHERE albums.Title LIKE 'Big Ones' 
  ORDER by tracks.Milliseconds DESC

3)SELECT name, UnitPrice FROM tracks
  ORDER by UnitPrice ASC LIMIT 10

4)SELECT t.name, g.name AS Genre, a.Title FROM tracks t
  JOIN albums a ON t.AlbumId = a.AlbumId 
  JOIN genres g ON t.GenreId = g.GenreId
  WHERE t.UnitPrice = 0.99

5)SELECT t.name, t.Milliseconds, a.Title, art.name AS Artista  FROM tracks t
  JOIN albums a ON t.AlbumId = a.AlbumId 
  JOIN genres g ON t.GenreId = g.GenreId
  JOIN artists art ON a.ArtistId = art.ArtistId
  ORDER by t.Milliseconds ASC LIMIT 20

6)SELECT emp.LastName AS empleado, jefe.LastName AS jefe, COUNT(*)  FROM employees emp
  JOIN employees jefe ON emp.ReportsTo = jefe.EmployeeId
  JOIN customers cus ON emp.EmployeeId = cus.SupportRepId
  GROUP BY emp.EmployeeId
  ORDER by jefe ASC

7)SELECT emp.FirstName AS Nombre_Empleado , emp.LastName AS Apellido_Empleado, c.FirstName AS Nombre_Cliente , c.LastName AS Apellido_Cliente FROM employees emp
  JOIN customers c ON emp.EmployeeId = c.SupportRepId
  ORDER by emp.LastName ASC

8)SELECT c.FirstName, c.LastName, c.Address, inv.InvoiceDate FROM customers c
  JOIN invoices inv ON c.CustomerId = inv.CustomerId

9)SELECT g.name, sum(t.TrackId) AS Canciones FROM genres g 
  JOIN tracks t ON g.GenreId = t.GenreId
  GROUP by g.GenreId

10)SELECT c.FirstName, inv.InvoiceDate, art.name FROM customers c
JOIN invoices inv ON c.CustomerId = inv.CustomerId
JOIN invoice_items inv_i ON inv.InvoiceId = inv_i.InvoiceId
JOIN tracks t ON inv_i.TrackId = t.TrackId
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN artists art ON a.ArtistId = art.ArtistId
ORDER by c.FirstName ASC

11)SELECT c.FirstName, c.City, t.name AS Song, g.name AS Genre FROM customers c
JOIN invoices inv ON c.CustomerId = inv.CustomerId
JOIN invoice_items inv_i ON inv.InvoiceId = inv_i.InvoiceId
JOIN tracks t ON inv_i.TrackId = t.TrackId
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN artists art ON a.ArtistId = art.ArtistId
JOIN genres g ON t.GenreId = g.GenreId

12)SELECT c.FirstName, c.City, t.name AS Song, g.name AS Genre FROM customers c
JOIN employees emp ON c.SupportRepId = emp.EmployeeId
JOIN invoices inv ON c.CustomerId = inv.CustomerId
JOIN invoice_items inv_i ON inv.InvoiceId = inv_i.InvoiceId
JOIN tracks t ON inv_i.TrackId = t.TrackId
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN artists art ON a.ArtistId = art.ArtistId
JOIN genres g ON t.GenreId = g.GenreId
JOIN playlist_track playlst ON t.TrackId = playlst.TrackId
JOIN playlists plist ON playlst.PlaylistId = plist.PlaylistId
JOIN media_types mt ON t.MediaTypeId = mt.MediaTypeId

