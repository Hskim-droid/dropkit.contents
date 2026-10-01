import skillCatalog from '../../skills/catalog.json';
import serviceCatalog from '../../services/catalog.json';
export const skills = skillCatalog.skills as { id: string; title: string; description: string; license: string }[];
export const services = serviceCatalog.services as { id: string; title: string; description: string; url: string }[];
