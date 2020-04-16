/*
Surge & QX MITM = tide-api.moreless.io
*/

let obj=JSON.parse($response.body)
obj.account["vip"]["is_lifetime_member"] = true;
$done({body:JSON.stringify(obj)})