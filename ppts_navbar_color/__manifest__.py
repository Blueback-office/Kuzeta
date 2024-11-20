{
    "name": "PPTS NavBar Company Color",
    "category": "web",
    "version": "17.0",
    "author": "PPTS [India] Pvt.Ltd.",
    "website": "http://www.pptssolutions.com",
    "depends": ["web","base_sparse_field","website"],
    "data": [
        'view/res_company.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'ppts_navbar_color/static/src/js/navbar.js',
            'ppts_navbar_color/static/src/scss/navbar.scss',

        ],
        'website.assets_editor': [
            'ppts_navbar_color/static/src/xml/**/*',
        ]
    },
    "license": "AGPL-3",
    'price': 33.5,
    'currency': 'USD',
    'images': ['static/description/banner.png'],
    "auto_install": False,
    "installable": True,
}
