
const routes = [
  {
    path: '/',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ]
  },
  {
    path: '/kviz-slika',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/kviz-slika.vue') }
    ]
  },
  {
    path: '/kviz-naziv',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/kviz-naziv.vue') }
    ]
  },
  {
    path: '/pregled',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/pregled.vue') }
    ]
  },
  {
    path: '/detalji',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/detaljibiljke.vue') }
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
