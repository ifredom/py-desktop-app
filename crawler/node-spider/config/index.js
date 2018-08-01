module.exports = {
    port: process.env.PORT ? process.env.PORT : 3007, // 端口号
    mongodb: 'mongodb://localhost:27017/spider', // 数据库地址
    session: {
        name: 'SID',
        secret: 'SID',
        cookie: {
            httpOnly: true,
            secure: false,
            maxAge: 365 * 24 * 60 * 60 * 1000
        }
    }
}