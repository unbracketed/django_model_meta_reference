
abstract
    TODO: need description

abstract_managers
    TODO: need description

add_field
    TODO: need description

add_virtual_field
    TODO: need description

admin
    TODO: need description

app_label
    TODO: need description

auto_created
    TODO: need description

auto_field
    TODO: need description

concrete_managers
    TODO: need description

contribute_to_class
    TODO: need description

db_table
    TODO: need description

db_tablespace
    TODO: need description

duplicate_targets
    TODO: need description

fields
    TODO: need description

get_add_permission
    TODO: need description

get_all_field_names
    Returns a list of all field names that are possible for this model (including reverse relation names). This is used for pretty printing debugging output (a list of choices), so any internal-only field names are not included. 

get_all_related_m2m_objects_with_model
    Returns a list of (related-m2m-object, model) pairs. Similar to get_fields_with_model(). 

get_all_related_many_to_many_objects
    TODO: need description

get_all_related_objects
    TODO: need description

get_all_related_objects_with_model
    Returns a list of (related-object, model) pairs. Similar to get_fields_with_model(). 

get_ancestor_link
    Returns the field on the current model which points to the given "ancestor". This is possible an indirect link (a pointer to a parent model, which points, eventually, to the ancestor). Used when constructing table joins for model inheritance. Returns None if the model isn't an ancestor of this one. 

get_base_chain
    Returns a list of parent classes leading to 'model' (order from closet to most distant ancestor). This has to handle the case were 'model' is a granparent or even more distant relation. 

get_change_permission
    TODO: need description

get_delete_permission
    TODO: need description

get_field
    Returns the requested field by name. Raises FieldDoesNotExist on error. 

get_field_by_name
    Returns the (field_object, model, direct, m2m), where field_object is the Field instance for the given name, model is the model containing this field (None for local fields), direct is True if the field exists on this model, and m2m is True for many-to-many relations. When 'direct' is False, 'field_object' is the corresponding RelatedObject for this field (since the field doesn't have an instance associated with it). Uses a cache internally, so after the first access, this is very fast. 

get_fields_with_model
    Returns a sequence of (field, model) pairs for all fields. The "model" element is None for fields on the current model. Mostly of use when constructing queries so that we know which model a field belongs to. 

get_latest_by
    TODO: need description

get_m2m_with_model
    The many-to-many version of get_fields_with_model(). 

get_ordered_objects
    Returns a list of Options objects that are ordered with respect to this object.

get_parent_list
    Returns a list of all the ancestor of this model as a list. Useful for determining if something is an ancestor, regardless of lineage. 

has_auto_field
    TODO: need description

init_name_map
    Initialises the field name -> field object mapping. 

installed
    TODO: need description

local_fields
    TODO: need description

local_many_to_many
    TODO: need description

managed
    TODO: need description

many_to_many
    TODO: need description

module_name
    TODO: need description

object_name
    TODO: need description

order_with_respect_to
    TODO: need description

ordering
    TODO: need description

parents
    TODO: need description

permissions
    TODO: need description

pk
    TODO: need description

pk_index
    Returns the index of the primary key field in the self.fields list. 

proxy
    TODO: need description

proxy_for_model
    TODO: need description

setup_pk
    TODO: need description

setup_proxy
    Does the internal setup so that the current model is a proxy for "target". 

unique_together
    TODO: need description

verbose_name
    TODO: need description

verbose_name_plural
    TODO: need description

verbose_name_raw
    TODO: need description

virtual_fields
    TODO: need description
