get_field_by_name
=================

   Returns the (field_object, model, direct, m2m), where field_object is the Field instance for the given name, model is the model containing this field (None for local fields), direct is True if the field exists on this model, and m2m is True for many-to-many relations. When 'direct' is False, 'field_object' is the corresponding RelatedObject for this field (since the field doesn't have an instance associated with it). Uses a cache internally, so after the first access, this is very fast. 
