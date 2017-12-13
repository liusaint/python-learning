

// var http=require('http');  
// //get 请求外网  
// http.get('http://www.runningls.com/demos/',function(req,res){  
//     var html='';  
//     req.on('data',function(data){  
//         html+=data;  
//     });  
//     req.on('end',function(){  
//         console.info(html);  
//     });  
// });  


//发送Post请求  
var http = require('http');
var querystring = require('querystring');
var data = {
    page: 1,
    order_type: 1,
    book_id: 4450
};
var post_data = querystring.stringify(data);

var options = {
    hostname: 'dev.ineln.integle.com',
    path: '/?r=book/experiment-list',
    method: 'POST',
    // port: '8888',
    headers: {

        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': Buffer.byteLength(post_data),
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',

        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'UM_distinctid=15fdde3fb583e3-0a9ea3e713d9c8-611d107f-1fa400-15fdde3fb594b4; gr_user_id=9c58fe65-98e8-4249-bad2-f161bd4c84cc; firstnew=1; _ga=GA1.2.359367017.1511320465; 589efa5385af02b31fc877e26b836971=1800; ygu=50141CD8E23DBAB2FD86207460CD6016; Hm_lvt_25e88d6ab9b8dbad58135718278933d1=1512784728,1512885075,1513043498,1513136083; Hm_lpvt_25e88d6ab9b8dbad58135718278933d1=1513137298; dev_ygu=0237A11242A56167809405105EAA3ECA; sims_u=64181c0c5ad631f47c9b869b0e2b01d7; CNZZDATA1255141213=1614237006-1501739920-http%253A%252F%252Fdev.center.integle.com%252F%7C1513149871; integle_session=53a81f62gp5j5ukpgt79ftvs63',

        'Origin': 'http://dev.ineln.integle.com',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://dev.ineln.integle.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'

    }
}




//创建请求  
var req = http.request(options, function(res) {
    console.log('STATUS:' + res.statusCode);
    // console.log('HEADERS:'+JSON.stringify(res.headers));  
    res.setEncoding('utf-8');
    res.on('data', function(chunk) {
        console.log('数据片段分隔-----------------------\r\n');
        console.log(chunk);
    });
    // res.on('end',function(){  
    //     console.log('响应结束********');  
    // });  

    var html = '';
    res.on('data', function(data) {
        html += data;
    });
    res.on('end', function() {
        console.info(html, 3);
    });
});
req.on('error', function(err) {
    console.error(err);
});
req.write(post_data);
req.end();



