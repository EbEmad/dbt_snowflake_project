select 
o.order_date,
o.order_id,
sum(total_price) as total_price
from 
{{ ref('stg_orders') }} o
left join
{{ ref('stg_order_items')}} oI
on o.order_id=oI.order_id
group by 1,2

