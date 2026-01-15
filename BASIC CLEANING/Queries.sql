PROJECT: Retail Sales Automation
AUTHOR: Muhammad Saad Amin

--Queries---
use retail_project;
select p.category, sum(f.sales) from fact_sales f join dim_products p on f.product_id= p.product_id group by p.category;
select p.city, sum(f.sales) from fact_sales f join dim_location p on p.location_id = f.location_id group by p.city;
select l.city, p.category, sum(f.sales) from fact_sales f 
join dim_location l on f.location_id = l.location_id
join dim_products p on f.product_id = p.product_id
where l.city = 'Henderson'
group by l.city, p.category;

select l.city, p.segment, sum(f.sales) as total_sales from fact_sales f 
join dim_location l on f.location_id = l.location_id
join dim_customers p on f.customer_id = p.customer_id
where f.sales > 1000
group by l.city, p.segment;

select l.city, p.category, sum(f.profit) as total_profit from fact_sales f 
join dim_location l on f.location_id = l.location_id
join dim_products p on f.product_id = p.product_id
where f.profit < 0
group by l.city , p.category;

select l.city, p.category, avg(f.discount) from fact_sales f 
join dim_location l on f.location_id = l.location_id
join dim_products p on f.product_id = p.product_id
where l.state = 'Texas'
group by l.city, p.category
having avg(discount) > 0.2;


