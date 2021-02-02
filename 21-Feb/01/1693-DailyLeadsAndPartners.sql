-- 2/1/21
-- 1693. Daily Leads and Partners
--  Question https://leetcode.com/problems/daily-leads-and-partners/submissions/

-- Write your MySQL query statement below
SELECT date_id, make_name,COUNT(DISTINCT(lead_id)) as unique_leads, COUNT(DISTINCT(partner_id)) as unique_partners
FROM DailySales
GROUP BY date_id,make_name