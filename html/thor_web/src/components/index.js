import Vue from 'vue'
import VHead from './Head'
import VFooter from './Footer'
import Sidebar from './Sidebar'

[
	VHead,
	VFooter,
	Sidebar
].forEach(Component => {
	Vue.component(Component.name, Component)
});
