-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- You should use attributes formed and split for computing the lifespan
-- Your script can be executed on any database

SELECT band_name
FROM metal_bands
WHERE style LIKE '%Glam rock%';