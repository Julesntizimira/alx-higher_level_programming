# include "lists.h"
/**
 * sum_dlistint - function that prints all the elements of a dlistint_t list.
 * @head: input node
 * Return: sum of element
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *tmp = NULL;
	int sum = 0;

	if (head == NULL)
		return (0);
	tmp = head;
	while (tmp != NULL)
	{
		sum += tmp->n;
		tmp = tmp->next;
	}
	return (sum);
}
