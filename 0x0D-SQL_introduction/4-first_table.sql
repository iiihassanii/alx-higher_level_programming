-- creates a table called first_table.
IF `first_table` NOT EXISTS CREATE TABLE `first_table`
{
        `id` (INT),
        `name` VARCHAR(256)
}