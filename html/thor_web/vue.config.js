let path = require('path');

function resolve (dir) {
	console.log(path.join(__dirname, dir))
	return path.join(__dirname, dir)
}

module.exports = {
	publicPath: process.env.NODE_ENV === 'production' ? '/html/' : '/',
	chainWebpack: config => {
		config.resolve.alias.set("~", resolve('src'))
	},
	devServer: {
		proxy: {
			'api': {
				target: 'thor.com/api', // 填写api地址,
				ws: true,
				changeOrigin: true,
				// pathRewrite: {
				// 	'^/api': ''
				// }
			}
		}
	}
}
