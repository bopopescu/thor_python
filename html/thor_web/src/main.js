import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import ElementUi from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import '~/assets/css/main.css'

import './components'

Vue.config.productionTip = false
Vue.use(ElementUi)

new Vue({
	router,
	store,
	...App
}).$mount('#app')
