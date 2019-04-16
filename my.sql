select vote.id as vote_id,user_id,plant_id,rank_id,vote_date,comment,vote,
rank.subject as rank_subject,rank.title as rank_title,rank.content as rank_content,
plant.user_id as plant_user,plant.category_id as plant_category,plant.name as plant_name,plant.address as plant_address,plant.avatar as plant_avatar,
user.name as user_name,user.email as user_email,user.phone as user_phone
from vote
inner join rank on vote.rank_id=rank_id
inner join plant on vote.plant_id=plant.id
inner join user on vote.user_id=user.id


select vote.id as vote_id,user_id,plant_id,rank_id,vote_date,comment,vote
from vote
inner join rank on vote.rank_id=rank.id
inner join plant on vote.plant_id=plant.id
inner join user on vote.user_id=user.id
