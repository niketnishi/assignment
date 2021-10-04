// Updates the new value to the provided query parameter
/*function update_query_parameter(query_parameter, update_dict) {
    let updated_query_parameter = "";
    let query_dict = {};
    let query_list = [];
    if(query_parameter !== "") {
        query_list = query_parameter.split('&');
    }
    for(let i = 0; i < query_list.length; i++) {
        query_dict[query_list[i].split('=')[0]] = query_list[i].split('=')[1];
    }
    for(let key_name in update_dict) {
        if(Object.keys(query_dict).includes(key_name)) {
            query_dict[key_name] = update_dict[key_name];
        } else {
            query_dict[key_name] = update_dict[key_name];
        }
    }
    for(let key in query_dict) {
        updated_query_parameter = updated_query_parameter + key + '=' + query_dict[key] + '&'
    }
    return updated_query_parameter.replace(new RegExp("^[&]+|[&]+$", "g"), "");
}*/
