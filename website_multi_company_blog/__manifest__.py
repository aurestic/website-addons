# -*- coding: utf-8 -*-
{
    "name": """Multi Website Blog""",
    "summary": """Blocks an access to a website blog from websites, which have not been specified as allowed for this blog""",
    "category": "eCommerce",
    # "live_test_url": "http://apps.it-projects.info/shop/product/website-multi-company?version=11.0",
    "images": ["images/multi_blog_main.png"],
    "version": "10.0.1.0.1",
    "application": False,
    "author": "IT-Projects LLC, Ildar Nasyrov",
    "support": "apps@itpp.dev",
    "website": "https://twitter.com/OdooFree",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["website_blog", "website_multi_company", "ir_rule_website"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/website_blog_views.xml", "security/blog_security.xml"],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
}
