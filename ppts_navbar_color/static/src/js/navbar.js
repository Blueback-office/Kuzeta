/** @odoo-module **/

import {NavBar} from "@web/webclient/navbar/navbar";
import {patch} from "@web/core/utils/patch";
import {session} from "@web/session";

document.addEventListener("DOMContentLoaded", function() {
    var elements = document.querySelectorAll(".o_main_navbar .o_menu_sections .o_nav_entry, .o_main_navbar .o_menu_sections .dropdown-toggle");
    elements.forEach(function(element) {
        element.style.setProperty("background", "none", "important");
    });
});

patch(NavBar.prototype, {
    get company_id() {
        return session.user_companies.color
    }
})
