Create TEMPORARY TABLE Res
AS 
select DISTINCT first.GoodId AS GoodId, first.Name AS GoodName, third.GTIN AS GTINs, four.CatId AS CatId, five.Name AS CatName
from Lst_Goods first, Lst_PartyPrices second, Lst_GTIN third, Lst_GoodsToCat four, Lst_Cat five
 where first.GoodId = second.GoodId and second.PartyId = 1 and first.Deleted = 0 and (third.GoodId = first.GoodId and third.GTINType = 1) and (first.GoodId = four.GoodId and four.CatId = five.CatId and five.left >=60000 and five.right <= 62833);

CREATE INDEX _GoodId ON Res (GoodId);

CREATE TABLE BET (id INT, ph INT NOT NULL DEFAULT 0, v INT NOT NULL DEFAULT 0); 
INSERT INTO BET (id) SELECT Lst_Goods.GoodId  FROM Lst_Goods;

Create temporary table ItogoPh as
SELECT DISTINCT a.GoodId, a.isPublished AS isPublished, a.Deleted AS Del, a.IsArchived AS Arch, a.Type AS Type
FROM Lst_Photos a
WHERE a.isPublished = 1 and a.Deleted = 0 and a.IsArchived = 0 and a.Type = '3ds';

Create temporary table ItogoV as
SELECT b.GoodId, b.AttrId AS VGH
FROM Lst_AttrValues b
WHERE b.AttrId BETWEEN 2437 AND 2440;

CREATE INDEX In_GoodId ON BET (id);
CREATE INDEX InPh_GoodId ON ItogoPh (Goodid);
CREATE INDEX InV_GoodId ON ItogoV (Goodid);


UPDATE BET INNER JOIN ItogoPh ON BET.id = ItogoPh.GoodId SET BET.photo = 1;
UPDATE BET INNER JOIN ItogoV ON BET.id = ItogoV.GoodId SET BET.vgh = 1;

select * from BET WHERE vgh = 1 and photo = 1;
Create TABLE Resu
AS 
select DISTINCT b.* , a.photo AS inPHOTO, a.vgh AS inVGH
from Res b, BET a
WHERE a.id = b.GoodId;

# rm spaces in GoodName
update Resu set GoodName = RTRIM (LTRIM(GoodName));

# rm LFCR in GoodName
update Resu set GoodName = REPLACE(REPLACE(GoodName, CHAR(10), ' '), CHAR(13), ' ');

# replace '\' to '/' in GoodName
update Resu set GoodName = REPLACE(GoodName, CHAR(92), CHAR(47));

# write into the file
SELECT * INTO OUTFILE '/tmp/result4.csv' FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' FROM Resu;
 
