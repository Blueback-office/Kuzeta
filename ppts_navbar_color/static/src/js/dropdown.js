/** @odoo-module **/

import { Dropdown } from "@web/core/dropdown/dropdown";
import {patch} from "@web/core/utils/patch";
import {session} from "@web/session";

patch(Dropdown.prototype,{
    get company_color(){
        return session.user_companies.color
    }
})
