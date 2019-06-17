const routes = [
  {
    path: '/',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
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
    path: '/test2',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/test2.vue') }
    ]
  },
  {
    path: '/unosslike',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Unosslike.vue') }
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
