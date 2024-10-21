with two_actor as (
  select actor1.actor_id as actor_id1
        , actor2.actor_id as actor_id2

  from film_actor as actor1, film_actor as actor2
    where actor1.film_id = actor2.film_id
      and actor1.actor_id < actor2.actor_id

  group by 1, 2
  order by count(actor1.film_id) desc
  limit 1
)
select
    (select first_name || ' ' || last_name from actor where actor_id = two_actor.actor_id1) as first_actor
    , (select first_name || ' ' || last_name from actor where actor_id = two_actor.actor_id2) as second_actor
    , film.title
from two_actor

    inner join film_actor  as film_actor1
      on two_actor.actor_id1 = film_actor1.actor_id
      
    inner join film_actor  as film_actor2
      on two_actor.actor_id2 = film_actor2.actor_id
      
    inner join film 
      on film_actor1.film_id = film.film_id 
        and film_actor2.film_id = film.film_id