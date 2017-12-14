//发送Post请求  
var http = require('http');
var zlib = require('zlib');

var options = {
    hostname: 'v3.wufazhuce.com',
    path: '/api/question/htmlcontent/1939?channel=huawei&sign=804684d4bbdc985bc59c5b6302c14eea&source=summary&source_id=14089&version=4.5.0&uuid=ffffffff-a0c5-1c61-d5d1-48ce0033c587&platform=android',
    method: 'GET',
    port: '8000',
    headers: {

        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': 0,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'User-Agent': 'android-async-http/2.0 (http://loopj.com/android-async-http)',
        'X-Requested-With': 'XMLHttpRequest'

    }
}



//创建请求  
var req = http.request(options, function(res) {

    var chunks = [];
    res.on('data', function(data) {
        chunks.push(data);
    });
    res.on('end', function() {

        var buffer = Buffer.concat(chunks);
        zlib.gunzip(buffer, function(err, decoded) {
            console.log(decoded.toString())
        })
    });
});
req.on('error', function(err) {
    console.error(err);
});

req.end();