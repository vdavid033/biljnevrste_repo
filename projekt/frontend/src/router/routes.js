
const routes = [
  {
    path: '/',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ]
  },
  {
    path: '/unostest',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/unos.vue') }
    ]
  },
  {
    path: '/unos',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Unos-Maria.vue') }
    ]
  },
  {
    path: '/kviz',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/kviz.vue') }
    ]
  },
  {
    path: '/kviz1',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Kviz-Maracic1.vue') }
    ]
  },
  {
    path: '/kviz2',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Kviz-Maracic2.vue') }
    ]
  },
  {
    path: '/test',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Test-Maracic.vue') }
    ]
  },
  {
    path: '/test-radio',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Test-radio-Maracic.vue') }
    ]
  },
  {
    path: '/pregled',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Pregled-Fures.vue') }
    ]
  },
  {
    path: '/biljne',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/BiljneVrsteRod.vue') }
    ]
  },
  {
    path: '/prikaz',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/prikaz.vue') }
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
