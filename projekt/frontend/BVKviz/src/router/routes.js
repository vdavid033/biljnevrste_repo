
const routes = [
  {
    path: '/',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ]
  },
  {
    path: '/kviz1',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/kviz1.vue') }
    ]
  },
  {
    path: '/kviz2',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/kviz2.vue') }
    ]
  },
  {
    path: '/test',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Test.vue') }
    ]
  },
  {
    path: '/test-radio',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Test-radio.vue') }
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
