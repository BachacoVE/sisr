update res_users
set active = False
where id in (select res_users.id from res_users
inner join for_dependencias
on res_users.dependencia_id = for_dependencias.id
where for_dependencias.dependencia ilike '%regi%'
and active is True)