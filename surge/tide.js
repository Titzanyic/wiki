/*
Surge & QX MITM = tide-api.moreless.io
*/

let obj=JSON.parse($response.body)
obj.vip["is_lifetime_member"] = true;
obj.vip["expired_at"] = 1585691786;
obj.vip["updated_at"] = 1585621786;
obj.vip["is_lifetime_member"] = 1585621786;
$done({body:JSON.stringify(obj)})