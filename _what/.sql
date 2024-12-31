with all_ships as (
  select country, name, bore from classes as c join ships as s on c.class=s.class
  union
  select country, ship, bore from classes as c join outcomes as o on c.class=o.ship
)
select
  all_ships.country, cast(round(avg(power(all_ships.bore,3)/2) as numeric(6, 2)), 2)
  from all_ships
  group by all_ships.country
