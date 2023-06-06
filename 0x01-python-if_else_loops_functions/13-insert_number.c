# include "lists.h"
# include <stdlib.h>
/**
 * insert_node - funct
 * @head: head node
 * @number: input number
 * Return: listint_t type
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *prev = NULL;

	tmp = *head;
	if (number <= tmp->n)
	{
		prev = malloc(sizeof(listint_t));
		if (prev == NULL)
			return (NULL);
		prev->n = number;
		prev->next = tmp;
		*head = prev;
		return (prev);
	}
	while (tmp != NULL)
	{
		if ((number >= tmp->n) && (tmp->next == NULL || number <= tmp->next->n ))
		{
			prev = malloc(sizeof(listint_t));
			if (prev == NULL)
				return (NULL);
			prev->n = number;
			if (tmp->next != NULL)
				prev->next = tmp->next;
			tmp->next = prev;
			return (prev);
		}
		tmp = tmp->next;
	}
	return (NULL);
}
