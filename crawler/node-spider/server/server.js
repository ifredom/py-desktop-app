const express = require('express')
const http = require('http')
const path = require('path');
const bodyParser = require('body-parser');
const serveStatic = require('serve-static');
const app = express();
const config = require('../config');
require('../database/mongodb.js'); // 连接数据库。 注释掉即可取消链接数据库
const main = require('../src/main');

app.all('*', (req, res, next) => {
  // 设置跨域
  res.header('Access-Control-Allow-Origin', req.headers.origin || '*');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Requested-With');
  res.header('Access-Control-Allow-Methods', 'PUT,POST,GET,DELETE,OPTIONS');
  res.header('X-Powered-By', '3.2.1');
  if (req.method == 'OPTIONS') {
    res.sendStatus(200)
  } else {
    next();
  }
});

app.set('views', path.join(__dirname, 'pages'));
app.set('view engine', 'pug');
app.use(serveStatic(path.join(__dirname, 'public')));
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
  extended: true
}));


app.get('/', function (req, res) {
  main() // 抓取
  res.sendFile(path.resolve(__dirname, '..', 'index.html'));
});

app.post('/', function (req, res) {
  res.send('抓取数据');
});

// 导出 app
if (module.parent) {
  module.exports = app;
} else {
  // 启动服务
  app.listen(config.port, function () {
    console.log(`\n Your application is running here: http://localhost:${config.port}\n`);
  });

}