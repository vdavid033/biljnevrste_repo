
const routes = [
  {
    path: '/',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ]
  },
  {
    path: '/play',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Play.vue') }
    ]
  },
  {
    path: '/unos',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/unos.vue') }
    ]
  },
  {
    path: '/test',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/test.vue') }
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
