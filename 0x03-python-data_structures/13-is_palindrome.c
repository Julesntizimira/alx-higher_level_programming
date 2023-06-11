# include "lists.h"
/**
 * is_palindrome - check for palindrome
 * @head: pointer to head of list
 * Return: 1 if the list is palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *tmp = NULL, *first = *head;
	listint_t *slow = *head, *h = NULL, *prev = NULL;

	if (*head == NULL || head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	while (1)
	{
		tmp = slow;
		if (fast == NULL)
		{
			tmp = tmp->next;
			break;
		}
		else if (fast->next == NULL)
		{
			tmp = tmp->next->next;
			break;
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	slow->next = NULL;
	while (tmp != NULL)
	{
		h = tmp;
		tmp = tmp->next;
		h->next = prev;
		prev = h;
	}
	tmp = h;
	while (first && tmp)
	{
		if (first->n != tmp->n)
			return (0);
		first = first->next;
		tmp = tmp->next;
	}
	return (1);
}
