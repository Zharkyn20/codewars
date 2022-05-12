def potatoes(p0, w0, p1):
    dry_matter = (100 - p0)*w0/100
    return (100 * dry_matter) // (100 - p1)
